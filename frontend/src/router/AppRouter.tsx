// src/AppRouter.tsx
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import Login from '../pages/auth/Login';
import Signup from '../pages/auth/Signup';
import VerifyEmail from '../pages/auth/VerifyEmail';
import TermsOfService from '../pages/auth/TermsOfService';
import SetupAccountType from '../pages/profile/setup/SetupAccountType';
import SetupPersonalInfo from '../pages/profile/setup/SetupPersonalInfo';
import SetupSocialLinks from '../pages/profile/setup/SetupSocialLinks';
import SetupCongratulations from '../pages/profile/setup/SetupCongratulations';
import Layout from '../pages/dashboard/components/Layout';
import LoadingScreen from '../components/LoadingScreen';
import PasswordReset from '../pages/auth/PasswordReset';
import ForgotPassword from '../pages/auth/ForgotPassword';
import DashboardView from '../pages/dashboard/DashboardView';
import AccountsView from '../pages/dashboard/AccountsView';
import AdsView from '../pages/dashboard/AdsView';
import AnalyzeView from '../pages/dashboard/AnalyzeView';
import CreateView from '../pages/dashboard/CreateView';
import FeedView from '../pages/dashboard/FeedView';
import InboxView from '../pages/dashboard/InboxView';
import ScheduleView from '../pages/dashboard/ScheduleView';
import TeamsView from '../pages/dashboard/TeamsView';
import SettingsView from '../pages/settings/SettingsView';

const PrivateRoute = ({ children }: { children: JSX.Element }) => {
    const { user, loading } = useAuth();
    if (loading) return <LoadingScreen/>; // or a proper loading component

    // Allow access to the dashboard in development mode
    const isDevMode = process.env.NODE_ENV === 'development';
    return user || isDevMode ? children : <Navigate to="/login" />;
};
// function to automatically create a new route with a Component inside the Layout and a private route
const CreatePrivateLayoutView = (component: React.ReactNode) => {
    return (
        <PrivateRoute>
            <Layout>
                {component}
            </Layout>
        </PrivateRoute>
    )
}

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
                <Route path="/password-reset/:uidb64/:token" element={<PasswordReset />} />
                <Route path="/forgot-password" element={<ForgotPassword />} />
                
                <Route path="/dashboard" element={CreatePrivateLayoutView(<DashboardView />)} />
                <Route path="/accounts" element={CreatePrivateLayoutView(<AccountsView />)} />
                <Route path='/ads' element={CreatePrivateLayoutView(<AdsView/>)} />
                <Route path='/analyze' element={CreatePrivateLayoutView(<AnalyzeView/>)} />
                <Route path='/create' element={CreatePrivateLayoutView(<CreateView/>)} />
                <Route path='/feed' element={CreatePrivateLayoutView(<FeedView/>)} />
                <Route path='/inbox' element={CreatePrivateLayoutView(<InboxView/>)} />
                <Route path='/schedule' element={CreatePrivateLayoutView(<ScheduleView/>)} />
                <Route path='/teams' element={CreatePrivateLayoutView(<TeamsView/>)} />
                {/* The settings page */}
                <Route path="/settings" element={CreatePrivateLayoutView(<SettingsView/>)} />
            </Routes>
        </Router>
    );
};


export default AppRouter;
