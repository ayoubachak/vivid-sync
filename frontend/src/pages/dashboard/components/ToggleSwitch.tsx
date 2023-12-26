// src/components/UI/ToggleSwitch.tsx

const ToggleSwitch: React.FC = () => {
    return (
      <label htmlFor="mode-switch" className="flex items-center cursor-pointer">
        <div className="relative">
          <input type="checkbox" id="mode-switch" className="sr-only" />
          <div className="block bg-gray-600 w-14 h-6 rounded-full"></div>
          <div className="dot absolute left-1 top-1 bg-white w-4 h-4 rounded-full transition"></div>
        </div>
      </label>
    );
  };
  
  export default ToggleSwitch;
  