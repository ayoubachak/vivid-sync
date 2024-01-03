// src/components/Dashboard/TopMenu.tsx

import { NOTIFICATION_BELL } from "../../../services/links/dashboard_icons";
import { useFetchUserInfo } from "../../../hooks/useFetchUserInfo";
import { FEMALE_ICON, MALE_ICON, ORANGE_TRIANGEL_DOWN } from "../../../services/links/icons";
import { MEDIA_URL } from "../../../services/links/links";
import { useEffect, useRef, useState } from "react";



interface TopMenuProps {

}

const TopMenu: React.FC<TopMenuProps> = () => {
    const [showUserDropdown, setShowUserDropdown] = useState(false);
    const [showNotificationDropdown, setShowNotificationDropdown] = useState(false);
    const { user, loading, error } = useFetchUserInfo();
    if(loading || error) {}

    const userMenuRef = useRef<HTMLDivElement>(null);
    const notificationMenuRef = useRef<HTMLDivElement>(null);

    const getProfilePicture = () => {
        if (!loading && !error) {
            if (user?.profilePicture) return MEDIA_URL +  user.profilePicture 
            return user?.gender === 'M'
                    ? MALE_ICON
                    : FEMALE_ICON;
        }
    }


    const handleUserClick = () => {
        setShowUserDropdown(!showUserDropdown);
      };
    
      const handleNotificationClick = () => {
        setShowNotificationDropdown(!showNotificationDropdown);
      };
    
      useEffect(() => {
        const handleClickOutside = (event: MouseEvent) => {
          // The event target needs to be cast as a Node here
          const target = event.target as Node;
          
          if (userMenuRef.current && !userMenuRef.current.contains(target)) {
            setShowUserDropdown(false);
          }
          if (notificationMenuRef.current && !notificationMenuRef.current.contains(target)) {
            setShowNotificationDropdown(false);
          }
        };
    
        document.addEventListener('mousedown', handleClickOutside);
        return () => {
          document.removeEventListener('mousedown', handleClickOutside);
        };
      }, []);

    return (
    <header className="flex justify-end gap-[26px] p-4 ">
           {/* Sidebar Toggle Button */}
        <div className="relative" ref={notificationMenuRef}>
            <div className="flex items-center justify-center w-10 h-10 rounded-full bg-white border-2 border-text-color p-[6px] hover:bg-gray-100 cursor-pointer"
                onClick={handleNotificationClick}>
              <img src={NOTIFICATION_BELL} alt="Notification" />
            </div>
            {showNotificationDropdown && (
            <div className="absolute right-0 mt-2 py-2 w-48 bg-white rounded-md shadow-xl">
                <a href="#" className="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100">Notification 1</a>
                {/* More notifications */}
            </div>
            )}
        </div>
 
        <div className="relative" ref={userMenuRef}>
            <div className="mr-6 flex gap-[6px] items-center hover:bg-gray-300 cursor-pointer transition duration-300 rounded-full"
                onClick={handleUserClick}>
            {!loading && <div className="flex items-center justify-center w-10 h-10 rounded-full bg-white transition duration-300">
                    <img src={getProfilePicture()} alt="Profile Picture" className="w-10 h-10 rounded-full" />
                </div>}
                <span className="text-slate-700 text-base font-normal">@{user?.username || "Gorlock"}</span>
                <div className="flex items-center">
                    <img src={ORANGE_TRIANGEL_DOWN} alt="Triangle Orange" className="w-4"/>
                </div>
            </div>
            {showUserDropdown && (
            <div className="absolute right-0 mt-2 py-2 w-48 bg-white rounded-md shadow-xl z-50">
                <a href="/profile/" className="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100">Profile</a>
                <a href="/settings/" className="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100">Settings</a>
                <a href="/logout/" className="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100">Log Out</a>
            </div>
            )}
        
      </div>

    </header>
  );
};

export default TopMenu;
