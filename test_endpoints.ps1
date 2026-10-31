Write-Output "=== 1. BACKEND DIRECT HEALTH CHECK ==="
$health = Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/health" -Method Get
Write-Output ($health | ConvertTo-Json -Depth 3)

Write-Output "`n=== 2. FRONTEND HTML LOAD ==="
$frontend = Invoke-WebRequest -Uri "http://localhost:5173/" -Method Get
Write-Output "Frontend HTTP Status: $($frontend.StatusCode)"
Write-Output "Frontend Content Length: $($frontend.Content.Length)"
Write-Output "Title tag found: $($frontend.Content -match '<title>(.*?)</title>')"
if ($matches) { Write-Output "Title: $($matches[1])" }

Write-Output "`n=== 3. FRONTEND PROXY HEALTH CHECK ==="
$proxyHealth = Invoke-RestMethod -Uri "http://localhost:5173/api/health" -Method Get
Write-Output ($proxyHealth | ConvertTo-Json -Depth 3)

Write-Output "`n=== 4. TEST CHAT REQUEST VIA FRONTEND PROXY ==="
$chatPayload = @{
    session_id = "verify-live-session-1"
    message = "ನನಗೆ 3 ಎಕರೆ ಅಡಿಕೆ ಜಮೀನು ಇದೆ, ಸಹಾಯಧನ ಬೇಕು"
    language = "kn"
} | ConvertTo-Json

$chatRes = Invoke-RestMethod -Uri "http://localhost:5173/api/chat" -Method Post -Body $chatPayload -ContentType "application/json; charset=utf-8"
Write-Output "Response Session ID: $($chatRes.session_id)"
Write-Output "Response Text KN: $($chatRes.response_text_kn)"
Write-Output "Extracted Crops: $($chatRes.updated_profile.crops -join ', ')"
Write-Output "Extracted Land Acres: $($chatRes.updated_profile.land_area.value_acres)"
Write-Output "Recommendations Count: $($chatRes.recommendations.Count)"

