import { LOGO_ICON } from "../services/links/icons";

const LoadingScreen: React.FC = () => {
    return (
      <div className="flex justify-center items-center h-screen">
        <img src={LOGO_ICON} alt="Loading..." className="logo-animation" />
      </div>
    );
  };
  
  export default LoadingScreen;