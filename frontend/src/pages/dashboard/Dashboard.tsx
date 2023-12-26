import React, { useState } from 'react';
import SideMenu from './components/SideMenu';
import TopMenu from './components/TopMenu';

const Dashboard: React.FC = () => {
  const [collapsed, setCollapsed] = useState(false);
  const toggleSidebar = () => setCollapsed(!collapsed);

  // Mock data for the stat cards, which you might fetch from an API in a real app
 
  return (
    <div className="flex h-screen">
    <SideMenu collapsed={collapsed} toggleSidebar={toggleSidebar} />
      <div className="flex-1 flex flex-col">
        <TopMenu />
        <main className="flex-1 overflow-x-hidden overflow-y-auto p-4">
          <div className="mb-4">
            <h1 className="text-2xl font-semibold text-gray-900">Home</h1>
            <p className="text-gray-600">Welcome back Gorlock 👋, Here is the recap!</p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
            {/* Statistic Cards */}
            
          </div>

          {/* Additional content here */}
        </main>
      </div>
    </div>
  );
};

export default Dashboard;
