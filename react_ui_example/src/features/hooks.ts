import { useCallback } from 'react';
import { useDispatch } from 'react-redux';
import { addSuppliers, setNextPageUrl } from './suppliersSlice';
import axios from 'axios';
// Import the types
import { Supplier, SuppliersResponse } from './types';

export const useSuppliers = () => {
    const dispatch = useDispatch();

    const fetchSuppliers = useCallback(async (search: string, city: string, nextPage: string | null) => {
        try {
            const baseUrl = `${process.env.REACT_APP_SERVER_URL}/app/v2/suppliers`;
            const url = nextPage || `${baseUrl}?country=1&lang=en&ordering=-popularity&search=${search}&city=${city}`;
            
            const response: any = await axios.get(url);
            dispatch(setNextPageUrl(response.data.next));
            dispatch(addSuppliers(response.data.results));
        } catch (error) {
            console.error('Failed to fetch suppliers:', error);
            // Handle error
        }
    }, [dispatch]);

    return { fetchSuppliers };
};
