// src/components/Dashboard/TopMenu.tsx

import ToggleSwitch from "./ToggleSwitch";
import { NOTIFICATION_BELL } from "../../../services/links/dashboard_icons";
import { useFetchUserInfo } from "../../../hooks/useFetchUserInfo";
import { FEMALE_ICON, MALE_ICON, ORANGE_TRIANGEL_DOWN } from "../../../services/links/icons";
import { MEDIA_URL } from "../../../services/links/links";



const TopMenu: React.FC = () => {

    const { user, loading, error } = useFetchUserInfo();
    if(loading || error) {

    }
    const getProfilePicture = () => {
        if (!loading && !error) {
            if (user?.profilePicture) return MEDIA_URL +  user.profilePicture 
            return user?.gender === 'M'
                    ? MALE_ICON
                    : FEMALE_ICON;
        }
    }
    return (
    <header className="flex justify-end gap-[26px] p-4 ">
      <ToggleSwitch />
      <div className="flex items-center justify-center w-10 h-10 rounded-full bg-white border-2 border-text-color p-[6px] hover:bg-gray-100 cursor-pointer">
        <img src={NOTIFICATION_BELL} alt="Notification" />
        </div>

        <div className="mr-6 flex gap-[6px] items-center hover:bg-gray-100 cursor-pointer transition duration-300">
            {!loading && <div className="flex items-center justify-center w-10 h-10 rounded-full bg-white transition duration-300">
                <img src={getProfilePicture()} alt="Profile Picture" className="w-10 h-10 rounded-full" />
            </div>}
            <span className="text-slate-700 text-base font-normal">@{user?.username || "Gorlock"}</span>
            <div className="flex items-center">
                <img src={ORANGE_TRIANGEL_DOWN} alt="Triangle Orange" className="w-4"/>
            </div>
        </div>

    </header>
  );
};

export default TopMenu;
