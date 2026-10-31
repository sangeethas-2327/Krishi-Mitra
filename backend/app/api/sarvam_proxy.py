import logging
import httpx
from fastapi import APIRouter, Request, Response, HTTPException
from ..config import settings

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/sarvam", tags=["sarvam-proxy"])

SARVAM_APP_RUNTIME_BASE = "https://apps.sarvam.ai/api/app-runtime"

@router.api_route("/{path:path}", methods=["GET", "POST", "OPTIONS", "HEAD"])
async def proxy_sarvam_runtime(path: str, request: Request):
    """
    Secure reverse proxy for Sarvam Conversational AI SDK.
    Injects SARVAM_API_KEY from backend environment variables into outgoing
    Sarvam runtime requests without exposing the private key to the browser.
    Preserves response status codes, headers, and signed WebSocket URLs.
    """
    api_key = settings.SARVAM_API_KEY.strip()
    
    # If in demo mode and no API key is provided, return informative error
    if not api_key:
        if settings.DEMO_MODE:
            logger.warning("SARVAM_API_KEY is not configured in backend .env. Live Sarvam agent proxy requires an API key.")
            return Response(
                content='{"detail": "SARVAM_API_KEY is not set in backend .env. Please configure your Sarvam API Key to use the live agent."}',
                status_code=401,
                media_type="application/json"
            )
        else:
            raise HTTPException(status_code=500, detail="SARVAM_API_KEY is not configured on the backend.")

    # Target URL on Sarvam App Runtime
    target_url = f"{SARVAM_APP_RUNTIME_BASE.rstrip('/')}/{path.lstrip('/')}"
    query_params = str(request.query_params)
    if query_params:
        target_url = f"{target_url}?{query_params}"

    # Build forward headers: inject secret API key into all potential auth headers
    api_key = settings.SARVAM_API_KEY.strip()

    forward_headers = {
        "X-API-Key": api_key,
        "api-subscription-key": api_key,
        "Authorization": f"Bearer {api_key}",
        "Content-Type": request.headers.get("Content-Type", "application/json"),
        "Accept": request.headers.get("Accept", "application/json"),
        "User-Agent": "Krishi-Mitra-App/1.0"
    }

    body = await request.body()

    try:
        async with httpx.AsyncClient(timeout=30.0, verify=False) as client:
            resp = await client.request(
                method=request.method,
                url=target_url,
                headers=forward_headers,
                content=body if request.method in ["POST", "PUT", "PATCH"] else None
            )

            if resp.status_code != 200:
                logger.warning(
                    f"Sarvam upstream returned HTTP {resp.status_code}: {resp.text[:300]}"
                )

            # Filter response headers to forward back safely
            excluded_headers = {"content-encoding", "content-length", "transfer-encoding", "connection"}
            response_headers = {
                k: v for k, v in resp.headers.items()
                if k.lower() not in excluded_headers
            }

            return Response(
                content=resp.content,
                status_code=resp.status_code,
                headers=response_headers,
                media_type=resp.headers.get("content-type", "application/json")
            )
    except httpx.TimeoutException:
        logger.error(f"Timeout while forwarding request to Sarvam: {target_url}")
        return Response(
            content='{"detail": "Timeout connecting to Sarvam conversational runtime."}',
            status_code=504,
            media_type="application/json"
        )
    except Exception as e:
        logger.error(f"Error proxying Sarvam request to {target_url}: {e}")
        return Response(
            content=f'{{"detail": "Failed to connect to Sarvam API: {str(e)}"}}',
            status_code=502,
            media_type="application/json"
        )

