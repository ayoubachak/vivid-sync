// src/AppRouter.tsx
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import Login from '../pages/auth/Login';
import Signup from '../pages/auth/Signup';
import Dashboard from '../pages/dashboard/Dashboard';
import VerifyEmail from '../pages/auth/VerifyEmail';
import TermsOfService from '../pages/auth/TermsOfService';
import SetupAccountType from '../pages/profile/setup/SetupAccountType';
import SetupPersonalInfo from '../pages/profile/setup/SetupPersonalInfo';
import SetupSocialLinks from '../pages/profile/setup/SetupSocialLinks';
import SetupCongratulations from '../pages/profile/setup/SetupCongratulations';
import Layout from '../pages/dashboard/components/Layout';
import LoadingScreen from '../components/LoadingScreen';

const PrivateRoute = ({ children }: { children: JSX.Element }) => {
    const { user, loading } = useAuth();
    if (loading) return <LoadingScreen/>; // or a proper loading component
    return user ? children : <Navigate to="/login" />;
};

const AppRouter = () => {
    return (
        <Router>
            <Routes>
                <Route path="/login" element={<Login />} />
                <Route path="/signup" element={<Signup />} />
                <Route path="/signup/verify-email" element={<VerifyEmail />} />
                <Route path="/terms-of-service" element={<TermsOfService />} />
                <Route path="/complete-profile/account-type" element={<SetupAccountType />} />
                <Route path="/complete-profile/personal-info" element={<SetupPersonalInfo />} />
                <Route path="/complete-profile/last-steps" element={<SetupSocialLinks />} />
                <Route path="/complete-profile/congratulations" element={<SetupCongratulations />} />
                
                <Route 
                    path="/dashboard" 
                    element={
                        <PrivateRoute>
                            <Layout>
                                <Dashboard />
                            </Layout>
                        </PrivateRoute>
                    } 
                />
            </Routes>
        </Router>
    );
};


export default AppRouter;
