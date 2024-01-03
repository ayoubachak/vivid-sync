// src/components/Layout.tsx
import React, { useEffect, useState } from 'react';
import SideMenu from './SideMenu';
import TopMenu from './TopMenu';

const isSmallScreen = () => window.innerWidth <= 768; // You can adjust the value as per your design

const Layout: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [collapsed, setCollapsed] = useState(isSmallScreen());

  useEffect(() => {
    const handleResize = () => {
      setCollapsed(isSmallScreen());
    };
  
    window.addEventListener('resize', handleResize);
    return () => window.removeEventListener('resize', handleResize);
  }, []);
  

  const toggleSidebar = () => setCollapsed(!collapsed);

  return (
    <div className="flex h-screen">
      <SideMenu collapsed={collapsed} toggleSidebar={toggleSidebar} />
      <div className="flex-1 flex flex-col">
        <TopMenu />
        <main className="flex-1 overflow-x-hidden overflow-y-auto p-4">
          {children}
        </main>
      </div>
    </div>
  );
};

export default Layout;