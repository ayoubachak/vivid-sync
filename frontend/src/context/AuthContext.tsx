import React, { createContext, useContext, useState, ReactNode } from 'react';

type AuthContextType = {
    user: any; 
    login: (user: any) => void; 
    logout: () => void;
};

const AuthContext = createContext<AuthContextType>(null!);

export const useAuth = () => useContext(AuthContext);

interface AuthProviderProps {
    children: ReactNode; // Explicitly type 'children'
}

export const AuthProvider: React.FC<AuthProviderProps> = ({ children }) => {
    const [user, setUser] = useState(null);

    const login = (userData: any) => {
        // Replace 'any' with your user type
        localStorage.setItem('accessToken', userData.access_token);
        localStorage.setItem('refreshToken', userData.refresh_token);
        setUser(userData.user);
    };

    const logout = () => {
        localStorage.removeItem('accessToken');
        localStorage.removeItem('refreshToken');
        setUser(null);
    };
    

    return (
        <AuthContext.Provider value={{ user, login, logout }}>
            {children}
        </AuthContext.Provider>
    );
};
