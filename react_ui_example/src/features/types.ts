export interface Supplier {
    id: number;
    name: string;
    name_en: string;
    license_number: string;
    status: string;
    logo: string;
    email: string;
    rating_score: number;
    rating_count: number;
    comments_count: number;
    popularity: number;
    city: number;
  }
  
  export interface SuppliersResponse {
    next: string | null;
    previous: string | null;
    results: Supplier[];
  }
  