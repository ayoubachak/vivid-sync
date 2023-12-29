// src/components/Dashboard/SideMenu.tsx
import React from 'react';
import { LOGO_ICON } from '../../../services/links/icons';
import { ACCOUNTS_ICON, ADS_ICON, ANALYSE_ICON, CREATE_ICON, FEED_ICON, HOME_ICON, INBOX_ICON, LOGOUT_ICON, SCHEDULE_ICON, SETTINGS_ICON,  TEAMS_ICON } from '../../../services/links/dashboard_icons';
import { useLocation } from 'react-router-dom';

interface SideMenuProps {
  collapsed: boolean;
  toggleSidebar: () => void;
  // Add any additional props needed for handling settings and logout actions
}

const SideMenu: React.FC<SideMenuProps> = ({ collapsed, toggleSidebar }) => {
  // Placeholder menu items data. Replace with your actual icons and labels\
  const location = useLocation();

  const menuItems = [
    { 
      icon: HOME_ICON, 
      label: 'Home', 
      link : '/dashboard/'
    },
    { 
      icon: CREATE_ICON, 
      label: 'Create',
      link : '/create/'
    },
    { 
      icon: INBOX_ICON,
      label: 'Inbox',
      link : '/inbox/'
    },
    { 
      icon: FEED_ICON,
      label: 'Feed',
      link : '/feed/'
    },
    { 
      icon: SCHEDULE_ICON,
      label: 'Schedule',
      link : '/schedule/'
    },
    { 
      icon: ANALYSE_ICON,
      label: 'Analyze',
      link : '/analyze'
    },
    { 
      icon: ADS_ICON,
      label: 'Ads',
      link : '/ads/'
    },
    { 
      icon: TEAMS_ICON,
      label: 'Teams',
      link : '/teams/'
    },
    { 
      icon: ACCOUNTS_ICON,
      label: 'Accounts',
      link : '/accounts/'
    },
    // Add other menu items if necessary
  ];

  return (
    <aside className={`sidebar ${collapsed ? 'w-20' : 'w-64'} transition-width duration-300 h-screen light text-white flex flex-col justify-between border-r-2 border-color-primary overflow-y-auto`}>
      <div >
        {/* Logo and Toggle Button */}
        <div 
          className="flex items-center justify-between p-4"
          onClick={toggleSidebar}
        >
          <img src={LOGO_ICON} alt="Logo"
              className={`transform transition-transform duration-300 ${collapsed ? 'rotate-90' : 'rotate-0'} cursor-pointer `} />
        </div>
        {/* Menu Items */}
        {menuItems.map((item, index) => (
          <a
            key={index}
            href={item.link}
            className={`flex items-center p-3 gap-4 ${collapsed ? 'justify-center' : 'justify-start'}
                        hover:bg-color-secondary hover:text-white transition-colors duration-300
                        ${location.pathname === item.link ? 'bg-color-secondary text-white' : 'text-[#878787]'}`}
          >
            <img src={item.icon} alt={item.label} className="w-6 h-6" />
            <span className={`${collapsed ? 'hidden' : 'block'}`}>{item.label}</span>
          </a>
        ))}

      </div>

      <div className="mt-auto">
        {/* Settings Button */}
        <a href="/settings/" className={`flex items-center p-3 gap-4 text-[#878787] ${collapsed ? 'justify-center' : 'justify-start'}`}>
          <img src={SETTINGS_ICON} alt="Settings" className="w-6 h-6" />
          <span className={`${collapsed ? 'hidden' : 'block'}`}>Settings</span>
        </a>
        {/* Logout Button */}
        <a href="/logout/" className={`flex items-center p-3 gap-4 text-color-secondary ${collapsed ? 'justify-center' : 'justify-start'}`}>
          <img src={LOGOUT_ICON} alt="Log Out" className="w-6 h-6" />
          <span className={`${collapsed ? 'hidden' : 'block'}`}>Log Out</span>
        </a>
      </div>
    </aside>
  );
};

export default SideMenu;
