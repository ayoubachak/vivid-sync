// src/components/Layout.tsx
import React, { useState } from 'react';
import SideMenu from './SideMenu';
import TopMenu from './TopMenu';

const Layout: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [collapsed, setCollapsed] = useState(false);
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