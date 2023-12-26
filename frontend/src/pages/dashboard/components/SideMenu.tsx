// src/components/Dashboard/SideMenu.tsx
interface SideMenuProps {
  collapsed: boolean;
  toggleSidebar: () => void; // Define a function type for the toggleSidebar prop
}

const SideMenu: React.FC<SideMenuProps> = ({ collapsed, toggleSidebar }) => {
    return (
      <aside className={`sidebar ${collapsed ? 'w-20' : 'w-64'} transition-width duration-300`}>
        {/* Menu items here */}
        <button onClick={toggleSidebar}>Toggle</button>
      </aside>
    );
  };
  
  export default SideMenu;
  