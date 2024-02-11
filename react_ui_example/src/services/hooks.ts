import { useState, useEffect } from 'react';
import axios from 'axios';

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
  



export const useSuppliers = (initialSearch: string = '', initialCity: string = '') => {
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string>('');
  const [suppliers, setSuppliers] = useState<Supplier[]>([]);
  const [nextPageUrl, setNextPageUrl] = useState<string | null>(null);

  const fetchSuppliers = async (search: string = initialSearch, city: string = initialCity, nextPage: string | null = null) => {
    setLoading(true);
    setError('');

    try {
      // Construct URL based on whether we're fetching the next page or starting anew
      const baseUrl = `${process.env.REACT_APP_SERVER_URL}/api/v2/cars`;
      const url = nextPage || `${baseUrl}?country=1&lang=en&ordering=-popularity&search=${search}&city=${city}`;
      
      const response = await axios.get<SuppliersResponse>(url);
      setSuppliers(prev => nextPage ? [...prev, ...response.data.results] : response.data.results);
      setNextPageUrl(response.data.next);
    } catch (err: any) {
      setError(err.message || 'An error occurred while fetching data.');
    } finally {
      setLoading(false);
    }
  };

  // Initial fetch
  useEffect(() => {
    fetchSuppliers();
  }, [initialSearch, initialCity]);

  return { loading, error, suppliers, fetchMore: () => nextPageUrl && fetchSuppliers(initialSearch, initialCity, nextPageUrl) };
};

