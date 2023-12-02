interface SocialButtonProps {
    children: React.ReactNode;
    icon: string;
    onClick: () => void;
}

export const SocialButton: React.FC<SocialButtonProps> = ({ children, icon, onClick }) => {
    return (
        <button
            className="font-bold h-[48px] bg-white rounded-[10px] border-2 border-slate-700 shadow appearance-none w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline flex items-center justify-start"
            onClick={onClick}
        >
            <img src={icon} width={33} height={33} alt={children ? children.toString() : "Icon"} className="mr-2" />
            {children}
        </button>
    );
};

