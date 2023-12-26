// src/components/Dashboard/StatCard.tsx

interface StatCardProps {
    title: string;
    value: string;
    icon: JSX.Element; // Use any icon library like react-icons
    trend: number; // Positive for increase, negative for decrease
  }
  
const StatCard: React.FC<StatCardProps> = ({ title, value, icon, trend }) => {
    const trendColor = trend > 0 ? 'text-green-500' : 'text-red-500';
    return (
        <div className="p-4 shadow rounded-lg bg-white">
        <div className="flex items-center justify-between">
            <div>
            <p className="text-gray-500">{title}</p>
            <p className="text-2xl font-bold">{value}</p>
            </div>
            {icon}
        </div>
        <div className={`flex items-center ${trendColor}`}>
            {trend > 0 ? '▲' : '▼'} {Math.abs(trend).toFixed(2)}%
        </div>
        </div>
    );
};

export default StatCard;
  