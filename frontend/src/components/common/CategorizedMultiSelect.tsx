import React, { useState, useRef, useEffect } from 'react';
import { Search, ChevronDown, X, Check, Plus, Tag } from 'lucide-react';

export interface MultiSelectItem {
  key: string;       // Normalized lowercase key
  name_en: string;
  name_kn: string;
}

export interface MultiSelectCategory {
  id: string;
  name_en: string;
  name_kn: string;
  items: MultiSelectItem[];
}

interface CategorizedMultiSelectProps {
  label: string;
  placeholder?: string;
  categories: MultiSelectCategory[];
  selectedKeys: string[];
  onChange: (keys: string[]) => void;
  language: 'kn' | 'en';
  allowOther?: boolean;
  otherKey?: string;
  otherPromptText?: string;
  customDetailValue?: string;
  onCustomDetailChange?: (val: string) => void;
  className?: string;
}

export const CategorizedMultiSelect: React.FC<CategorizedMultiSelectProps> = ({
  label,
  placeholder = 'Select items...',
  categories,
  selectedKeys,
  onChange,
  language,
  allowOther = true,
  otherKey = 'other',
  otherPromptText,
  customDetailValue = '',
  onCustomDetailChange,
  className = ''
}) => {
  const [isOpen, setIsOpen] = useState(false);
  const [searchTerm, setSearchTerm] = useState('');
  const [customInput, setCustomInput] = useState('');
  const [showCustomInput, setShowCustomInput] = useState(false);
  const containerRef = useRef<HTMLDivElement>(null);
  const searchInputRef = useRef<HTMLInputElement>(null);

  // Close on outside click
  useEffect(() => {
    const handleClickOutside = (event: MouseEvent) => {
      if (containerRef.current && !containerRef.current.contains(event.target as Node)) {
        setIsOpen(false);
      }
    };
    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, []);

  // Map of all items for fast lookup
  const itemMap = new Map<string, MultiSelectItem>();
  categories.forEach((cat) => {
    cat.items.forEach((item) => {
      itemMap.set(item.key.toLowerCase(), item);
    });
  });

  // Toggle item selection
  const handleToggle = (key: string) => {
    const normKey = key.toLowerCase();
    if (selectedKeys.includes(normKey)) {
      onChange(selectedKeys.filter((k) => k.toLowerCase() !== normKey));
    } else {
      onChange([...selectedKeys, normKey]);
    }
  };

  const handleRemoveChip = (keyToRemove: string, e: React.MouseEvent) => {
    e.stopPropagation();
    onChange(selectedKeys.filter((k) => k.toLowerCase() !== keyToRemove.toLowerCase()));
  };

  const handleAddCustomChip = () => {
    if (!customInput.trim()) return;
    const cleanKey = customInput.trim().toLowerCase();
    if (!selectedKeys.includes(cleanKey)) {
      onChange([...selectedKeys, cleanKey]);
    }
    setCustomInput('');
    setShowCustomInput(false);
  };

  // Filter categories and items based on search term
  const term = searchTerm.trim().toLowerCase();
  const filteredCategories = categories
    .map((cat) => {
      const catMatches =
        cat.name_en.toLowerCase().includes(term) || cat.name_kn.includes(term);
      const filteredItems = cat.items.filter((item) => {
        if (!term) return true;
        return (
          catMatches ||
          item.name_en.toLowerCase().includes(term) ||
          item.name_kn.includes(term) ||
          item.key.toLowerCase().includes(term)
        );
      });
      return { ...cat, items: filteredItems };
    })
    .filter((cat) => cat.items.length > 0);

  const isOtherSelected = selectedKeys.some((k) => k.toLowerCase() === otherKey.toLowerCase());

  return (
    <div className={`relative ${className}`} ref={containerRef}>
      <div className="flex items-center justify-between mb-1">
        <label className="block text-xs font-semibold text-[#282C27] font-kannada">
          {label}
        </label>
        {selectedKeys.length > 0 && (
          <span className="text-[10px] text-[#727B70] font-mono">
            {selectedKeys.length} {language === 'kn' ? 'ಆಯ್ಕೆಮಾಡಲಾಗಿದೆ' : 'selected'}
          </span>
        )}
      </div>

      {/* Selected Chips Area */}
      <div
        onClick={() => {
          setIsOpen((prev) => !prev);
          setTimeout(() => searchInputRef.current?.focus(), 50);
        }}
        className={`w-full bg-[#FAF7F0] border rounded-xl p-2 min-h-[42px] cursor-pointer transition-colors shadow-sm flex flex-wrap gap-1.5 items-center ${
          isOpen
            ? 'border-[#183B2B] ring-1 ring-[#183B2B]'
            : 'border-[#E2D9C8] hover:border-[#183B2B]/60'
        }`}
      >
        {selectedKeys.length > 0 ? (
          selectedKeys.map((key) => {
            const item = itemMap.get(key.toLowerCase());
            const displayKn = item ? item.name_kn : key;
            const displayEn = item ? item.name_en : key;
            return (
              <span
                key={key}
                className="inline-flex items-center space-x-1 px-2.5 py-1 rounded-lg bg-[#183B2B] text-white text-xs font-medium shadow-xs"
              >
                <Tag className="w-2.5 h-2.5 text-[#D7A85B] mr-0.5" />
                <span className="font-kannada">{language === 'kn' ? displayKn : displayEn}</span>
                {item && (
                  <span className="text-[10px] text-[#A8B58A] opacity-90 hidden sm:inline">
                    ({language === 'kn' ? displayEn : displayKn})
                  </span>
                )}
                <button
                  type="button"
                  onClick={(e) => handleRemoveChip(key, e)}
                  className="ml-1 text-white/70 hover:text-white p-0.5 rounded-full hover:bg-black/20 transition"
                >
                  <X className="w-3 h-3" />
                </button>
              </span>
            );
          })
        ) : (
          <span className="text-xs text-[#727B70] px-1 font-sans">{placeholder}</span>
        )}

        <div className="ml-auto pr-1 flex items-center">
          <ChevronDown
            className={`w-4 h-4 text-[#727B70] transition-transform ${
              isOpen ? 'transform rotate-180 text-[#183B2B]' : ''
            }`}
          />
        </div>
      </div>

      {/* Specific Custom Description Input if 'other' is selected */}
      {isOtherSelected && allowOther && onCustomDetailChange && (
        <div className="mt-2 p-3 bg-[#FAF7F0] border border-[#D7A85B]/60 rounded-xl space-y-1.5 animate-fadeIn">
          <label className="block text-[11px] font-bold text-[#183B2B] font-kannada">
            {otherPromptText ||
              (language === 'kn'
                ? 'ದಯವಿಟ್ಟು ನಿಮಗೆ ಅಗತ್ಯವಿರುವ ನೆರವನ್ನು ವಿವರವಾಗಿ ನಮೂದಿಸಿ (Please specify):'
                : 'Please specify the assistance you need:')}
          </label>
          <input
            type="text"
            value={customDetailValue}
            onChange={(e) => onCustomDetailChange(e.target.value)}
            placeholder={
              language === 'kn'
                ? 'ಉದಾ: ಸೋಲಾರ್ ಡ್ರೈಯರ್, ಕೃಷಿ ಸಂಸ್ಕರಣಾ ಸಾಲ...'
                : 'e.g., Solar dryer, processing grant, fencing...'
            }
            className="w-full bg-white border border-[#E2D9C8] rounded-lg p-2 text-xs text-[#282C27] focus:outline-none focus:border-[#183B2B]"
          />
        </div>
      )}

      {/* Dropdown Options Panel */}
      {isOpen && (
        <div className="absolute left-0 right-0 top-full mt-1.5 z-50 bg-white border border-[#E2D9C8] rounded-2xl shadow-xl overflow-hidden animate-fadeIn">
          {/* Search Header */}
          <div className="p-2.5 border-b border-[#E2D9C8] bg-[#FAF7F0] flex items-center space-x-2">
            <Search className="w-3.5 h-3.5 text-[#727B70] flex-shrink-0" />
            <input
              ref={searchInputRef}
              type="text"
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              placeholder={
                language === 'kn'
                  ? 'ಬೆಳೆ ಅಥವಾ ಅಗತ್ಯವನ್ನು ಹುಡುಕಿ...'
                  : 'Type to filter categories or items...'
              }
              className="w-full bg-transparent text-xs text-[#282C27] focus:outline-none placeholder-[#727B70]"
              onClick={(e) => e.stopPropagation()}
            />
            {searchTerm && (
              <button
                type="button"
                onClick={() => setSearchTerm('')}
                className="text-[#727B70] hover:text-[#282C27] text-xs p-0.5"
              >
                <X className="w-3 h-3" />
              </button>
            )}
          </div>

          {/* Categorized Items List */}
          <div className="max-h-64 overflow-y-auto divide-y divide-gray-100 scrollbar-thin">
            {filteredCategories.length > 0 ? (
              filteredCategories.map((cat) => (
                <div key={cat.id} className="py-2">
                  {/* Category Header */}
                  <div className="px-3 py-1 bg-[#EBE5D8]/40 text-[11px] font-bold text-[#183B2B] flex items-center justify-between tracking-wide font-kannada">
                    <span>{language === 'kn' ? cat.name_kn : cat.name_en}</span>
                    <span className="text-[10px] font-mono text-[#727B70]">
                      ({cat.items.length})
                    </span>
                  </div>

                  {/* Items in this category */}
                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-0.5 px-1 py-1">
                    {cat.items.map((item) => {
                      const isSelected = selectedKeys.some(
                        (k) => k.toLowerCase() === item.key.toLowerCase()
                      );
                      return (
                        <div
                          key={item.key}
                          onClick={() => handleToggle(item.key)}
                          className={`px-2.5 py-1.5 rounded-lg text-xs cursor-pointer flex items-center justify-between transition-colors ${
                            isSelected
                              ? 'bg-[#183B2B]/10 text-[#183B2B] font-bold'
                              : 'hover:bg-[#FAF7F0] text-[#282C27]'
                          }`}
                        >
                          <div className="truncate pr-1">
                            <span className="font-kannada">
                              {language === 'kn' ? item.name_kn : item.name_en}
                            </span>
                            <span className="text-[10px] text-[#727B70] ml-1.5 font-sans">
                              {language === 'kn' ? item.name_en : item.name_kn}
                            </span>
                          </div>
                          <div
                            className={`w-4 h-4 rounded border flex items-center justify-center flex-shrink-0 transition-colors ${
                              isSelected
                                ? 'bg-[#183B2B] border-[#183B2B] text-white'
                                : 'border-[#E2D9C8] bg-white'
                            }`}
                          >
                            {isSelected && <Check className="w-3 h-3 stroke-[2.5]" />}
                          </div>
                        </div>
                      );
                    })}
                  </div>
                </div>
              ))
            ) : (
              <div className="p-4 text-center text-xs text-[#727B70]">
                {language === 'kn'
                  ? 'ಯಾವುದೇ ಫಲಿತಾಂಶ ದೊರೆತಿಲ್ಲ'
                  : 'No matching items found'}
              </div>
            )}

            {/* Custom Entry Option ("Other" or Custom Type) */}
            {allowOther && (
              <div className="p-2.5 bg-[#FAF7F0] border-t border-[#E2D9C8]">
                {!showCustomInput ? (
                  <button
                    type="button"
                    onClick={(e) => {
                      e.stopPropagation();
                      setShowCustomInput(true);
                      setCustomInput(searchTerm);
                    }}
                    className="w-full text-left text-xs font-semibold text-[#183B2B] hover:underline flex items-center justify-between"
                  >
                    <span className="flex items-center space-x-1">
                      <Plus className="w-3.5 h-3.5 text-[#B08233]" />
                      <span>
                        {language === 'kn'
                          ? '+ ಇತರ ಬೆಳೆ / ಅಗತ್ಯವನ್ನು ನಮೂದಿಸಿ (Add custom option)'
                          : '+ Add custom option'}
                      </span>
                    </span>
                    <span className="text-[10px] bg-[#EBE5D8] px-2 py-0.5 rounded font-mono text-[#183B2B]">
                      Custom
                    </span>
                  </button>
                ) : (
                  <div className="space-y-2" onClick={(e) => e.stopPropagation()}>
                    <span className="text-[10px] font-bold text-[#183B2B] block">
                      {language === 'kn'
                        ? 'ಹೆಸರನ್ನು ಟೈಪ್ ಮಾಡಿ (Type custom name):'
                        : 'Type custom item name:'}
                    </span>
                    <div className="flex items-center space-x-1.5">
                      <input
                        type="text"
                        value={customInput}
                        onChange={(e) => setCustomInput(e.target.value)}
                        placeholder="Custom crop / need"
                        className="flex-1 bg-white border border-[#E2D9C8] rounded-lg px-2.5 py-1 text-xs text-[#282C27] focus:outline-none focus:border-[#183B2B]"
                        autoFocus
                      />
                      <button
                        type="button"
                        onClick={handleAddCustomChip}
                        disabled={!customInput.trim()}
                        className="px-2.5 py-1 bg-[#183B2B] text-white rounded-lg text-xs font-bold disabled:opacity-50"
                      >
                        {language === 'kn' ? 'ಸೇರಿಸಿ' : 'Add'}
                      </button>
                      <button
                        type="button"
                        onClick={() => setShowCustomInput(false)}
                        className="px-2 py-1 text-[#727B70] hover:text-[#282C27] text-xs"
                      >
                        ✕
                      </button>
                    </div>
                  </div>
                )}
              </div>
            )}
          </div>
        </div>
      )}
    </div>
  );
};

