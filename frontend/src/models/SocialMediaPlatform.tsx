export default interface SocialMediaPlatform {
    name: string;
    icon: string;
    baseUrl: string;
    loginRedirectUrl: string;
    loginCallbackUrl: string;
}