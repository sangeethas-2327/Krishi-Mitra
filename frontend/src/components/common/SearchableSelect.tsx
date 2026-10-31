import React, { useState, useRef, useEffect } from 'react';
import { Search, ChevronDown, X, Check } from 'lucide-react';

export interface SelectOption {
  id: string;
  name_en: string;
  name_kn: string;
  sublabel?: string;
}

interface SearchableSelectProps {
  label: string;
  placeholder?: string;
  options: SelectOption[];
  selectedValue: string; // id or custom value
  onSelect: (option: SelectOption | null, customText?: string) => void;
  disabled?: boolean;
  disabledHint?: string;
  language: 'kn' | 'en';
  allowCustomEntry?: boolean;
  customEntryLabel?: string;
  className?: string;
}

export const SearchableSelect: React.FC<SearchableSelectProps> = ({
  label,
  placeholder = 'Select...',
  options,
  selectedValue,
  onSelect,
  disabled = false,
  disabledHint,
  language,
  allowCustomEntry = false,
  customEntryLabel,
  className = ''
}) => {
  const [isOpen, setIsOpen] = useState(false);
  const [searchTerm, setSearchTerm] = useState('');
  const [isCustomMode, setIsCustomMode] = useState(false);
  const [customText, setCustomText] = useState('');
  const containerRef = useRef<HTMLDivElement>(null);
  const inputRef = useRef<HTMLInputElement>(null);

  // Close when clicking outside
  useEffect(() => {
    const handleClickOutside = (event: MouseEvent) => {
      if (containerRef.current && !containerRef.current.contains(event.target as Node)) {
        setIsOpen(false);
      }
    };
    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, []);

  // Find currently selected option
  const selectedOption = options.find(
    (opt) =>
      opt.id.toLowerCase() === selectedValue.toLowerCase() ||
      opt.name_en.toLowerCase() === selectedValue.toLowerCase() ||
      opt.name_kn === selectedValue
  );

  // Filter options based on search query
  const filteredOptions = options.filter((opt) => {
    if (!searchTerm.trim()) return true;
    const term = searchTerm.toLowerCase();
    return (
      opt.name_en.toLowerCase().includes(term) ||
      opt.name_kn.includes(term) ||
      (opt.sublabel && opt.sublabel.toLowerCase().includes(term))
    );
  });

  const handleSelectOption = (option: SelectOption) => {
    setIsCustomMode(false);
    onSelect(option);
    setIsOpen(false);
    setSearchTerm('');
  };

  const handleClear = (e: React.MouseEvent) => {
    e.stopPropagation();
    setIsCustomMode(false);
    setCustomText('');
    onSelect(null);
  };

  const handleApplyCustom = () => {
    if (!customText.trim()) return;
    onSelect(
      {
        id: customText.trim().toLowerCase(),
        name_en: customText.trim(),
        name_kn: customText.trim()
      },
      customText.trim()
    );
    setIsCustomMode(false);
    setIsOpen(false);
  };

  return (
    <div className={`relative ${className}`} ref={containerRef}>
      <label className="block text-xs font-semibold text-[#282C27] mb-1 font-kannada">
        {label}
      </label>

      {/* Trigger Box */}
      <div
        onClick={() => {
          if (!disabled) {
            setIsOpen((prev) => !prev);
            setTimeout(() => inputRef.current?.focus(), 50);
          }
        }}
        className={`w-full bg-[#FAF7F0] border rounded-xl p-2.5 text-xs flex items-center justify-between cursor-pointer transition-colors shadow-sm ${
          disabled
            ? 'opacity-60 bg-[#EBE5D8]/50 border-[#E2D9C8] cursor-not-allowed text-[#727B70]'
            : isOpen
            ? 'border-[#183B2B] ring-1 ring-[#183B2B] text-[#282C27]'
            : 'border-[#E2D9C8] hover:border-[#183B2B]/60 text-[#282C27]'
        }`}
      >
        <div className="flex-1 truncate pr-2">
          {selectedValue ? (
            <div className="flex items-center space-x-1.5 truncate">
              <span className="font-bold text-[#183B2B]">
                {language === 'kn'
                  ? selectedOption?.name_kn || selectedValue
                  : selectedOption?.name_en || selectedValue}
              </span>
              {selectedOption && (
                <span className="text-[10px] text-[#727B70] font-normal truncate">
                  ({language === 'kn' ? selectedOption.name_en : selectedOption.name_kn})
                </span>
              )}
            </div>
          ) : (
            <span className="text-[#727B70] font-normal font-sans">
              {disabled ? (disabledHint || placeholder) : placeholder}
            </span>
          )}
        </div>

        <div className="flex items-center space-x-1 flex-shrink-0">
          {selectedValue && !disabled && (
            <button
              type="button"
              onClick={handleClear}
              className="p-1 hover:bg-[#EBE5D8] rounded-md text-[#727B70] hover:text-[#183B2B] transition"
            >
              <X className="w-3.5 h-3.5" />
            </button>
          )}
          <ChevronDown
            className={`w-4 h-4 text-[#727B70] transition-transform ${
              isOpen ? 'transform rotate-180 text-[#183B2B]' : ''
            }`}
          />
        </div>
      </div>

      {/* Disabled explanatory hint below input if any */}
      {disabled && disabledHint && (
        <p className="text-[10px] text-[#727B70] mt-1 italic font-sans">{disabledHint}</p>
      )}

      {/* Dropdown Menu Panel */}
      {isOpen && !disabled && (
        <div className="absolute left-0 right-0 top-full mt-1.5 z-50 bg-white border border-[#E2D9C8] rounded-2xl shadow-xl overflow-hidden animate-fadeIn">
          {/* Search Input Filter */}
          <div className="p-2 border-b border-[#E2D9C8] bg-[#FAF7F0] flex items-center space-x-2">
            <Search className="w-3.5 h-3.5 text-[#727B70] flex-shrink-0" />
            <input
              ref={inputRef}
              type="text"
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              placeholder={language === 'kn' ? 'ಹುಡುಕಿ (Search)...' : 'Type to search...'}
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

          {/* Options List */}
          <div className="max-h-56 overflow-y-auto divide-y divide-gray-50 scrollbar-thin">
            {filteredOptions.length > 0 ? (
              filteredOptions.map((opt) => {
                const isSelected =
                  opt.id.toLowerCase() === selectedValue.toLowerCase() ||
                  opt.name_en.toLowerCase() === selectedValue.toLowerCase() ||
                  opt.name_kn === selectedValue;
                return (
                  <div
                    key={opt.id}
                    onClick={() => handleSelectOption(opt)}
                    className={`px-3 py-2.5 text-xs cursor-pointer flex items-center justify-between transition-colors ${
                      isSelected
                        ? 'bg-[#183B2B]/10 text-[#183B2B] font-bold'
                        : 'hover:bg-[#FAF7F0] text-[#282C27]'
                    }`}
                  >
                    <div>
                      <div className="font-medium font-kannada">
                        {language === 'kn' ? opt.name_kn : opt.name_en}
                      </div>
                      <div className="text-[10px] text-[#727B70] font-sans">
                        {language === 'kn' ? opt.name_en : opt.name_kn}
                        {opt.sublabel ? ` • ${opt.sublabel}` : ''}
                      </div>
                    </div>
                    {isSelected && (
                      <Check className="w-4 h-4 text-[#183B2B] flex-shrink-0 ml-2" />
                    )}
                  </div>
                );
              })
            ) : (
              <div className="p-3 text-center text-xs text-[#727B70] font-sans">
                {language === 'kn'
                  ? 'ಯಾವುದೂ ಕಂಡುಬಂದಿಲ್ಲ (No matches found)'
                  : 'No matches found'}
              </div>
            )}

            {/* Custom Entry Option (e.g. Village manual entry) */}
            {allowCustomEntry && (
              <div className="p-2.5 bg-[#FAF7F0] border-t border-[#E2D9C8]">
                {!isCustomMode ? (
                  <button
                    type="button"
                    onClick={(e) => {
                      e.stopPropagation();
                      setIsCustomMode(true);
                      setCustomText(searchTerm);
                    }}
                    className="w-full text-left text-xs font-semibold text-[#183B2B] hover:underline flex items-center justify-between"
                  >
                    <span>
                      {customEntryLabel ||
                        (language === 'kn'
                          ? '+ ಪಟ್ಟಿಯಲ್ಲಿಲ್ಲದ ಗ್ರಾಮವನ್ನು ನಮೂದಿಸಿ'
                          : '+ Enter manually if not in list')}
                    </span>
                    <span className="text-[10px] bg-[#EBE5D8] px-2 py-0.5 rounded font-mono text-[#183B2B]">
                      Custom
                    </span>
                  </button>
                ) : (
                  <div className="space-y-2" onClick={(e) => e.stopPropagation()}>
                    <span className="text-[10px] font-bold text-[#183B2B] block">
                      {language === 'kn' ? 'ಗ್ರಾಮದ ಹೆಸರು ಟೈಪ್ ಮಾಡಿ:' : 'Type Village Name:'}
                    </span>
                    <div className="flex items-center space-x-1.5">
                      <input
                        type="text"
                        value={customText}
                        onChange={(e) => setCustomText(e.target.value)}
                        placeholder="Village name"
                        className="flex-1 bg-white border border-[#E2D9C8] rounded-lg px-2.5 py-1 text-xs text-[#282C27] focus:outline-none focus:border-[#183B2B]"
                        autoFocus
                      />
                      <button
                        type="button"
                        onClick={handleApplyCustom}
                        disabled={!customText.trim()}
                        className="px-2.5 py-1 bg-[#183B2B] text-white rounded-lg text-xs font-bold disabled:opacity-50"
                      >
                        {language === 'kn' ? 'ಸೇರಿಸಿ' : 'Add'}
                      </button>
                      <button
                        type="button"
                        onClick={() => setIsCustomMode(false)}
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

