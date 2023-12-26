export enum AccountType {
    Influencer = 'Influencer',
    ContentCreator = 'Content Creator',
    Organization = 'Organization',
}
export type Gender = 'M' | 'F';
export interface VividUser {
    id: number;
    username: string;
    email: string;
    first_name: string;
    last_name: string;
    gender : Gender | null;
    createdAt: Date;
    updatedAt: Date;
    profilePicture?: string; // Assuming the URL to the image is sent as a string
    emailVerified: boolean;
    bio?: string;
    verification_code?: string;
    verification_token?: string;
    agreed_to_terms: boolean;
    account_type?: AccountType | null; // Use 'null' for the Django 'None' equivalent
    profile_completed: boolean;
}
  