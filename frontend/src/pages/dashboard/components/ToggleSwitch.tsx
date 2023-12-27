import React, { useState, useEffect } from 'react';

const ToggleSwitch: React.FC = () => {
  const [darkMode, setDarkMode] = useState(false);

  useEffect(() => {
    if (darkMode) {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
  }, [darkMode]);

  const handleModeChange = () => {
    setDarkMode(!darkMode);
  };

  return (
    <label htmlFor="mode-switch" className="flex items-center cursor-pointer">
      <div className="relative">
        <input
          type="checkbox"
          id="mode-switch"
          className="sr-only"
          onChange={handleModeChange}
          checked={darkMode}
        />
        <div
          className={`block w-14 h-6 rounded-full transition-colors duration-300 ${
            darkMode ? 'bg-intense-orange' : 'bg-light-orange'
          }`}
        ></div>
        <div
          className={`dot absolute left-1 top-1 bg-white w-4 h-4 rounded-full transition transform ${
            darkMode ? 'translate-x-8' : ''
          }`}
        ></div>
      </div>
    </label>
  );
};

export default ToggleSwitch;