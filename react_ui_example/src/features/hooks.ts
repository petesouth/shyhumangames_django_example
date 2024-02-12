import { useCallback } from 'react';
import { useDispatch } from 'react-redux';
import { addSuppliers, setNextPageUrl } from './suppliersSlice';
import axios from 'axios';
// Import the types
import { SuppliersResponse } from './types';

export const useSuppliers = () => {
    const dispatch = useDispatch();

    const fetchSuppliers = useCallback(async (search: string, city: string, nextPage: string | null) => {
        try {
            const baseUrl = `${process.env.REACT_APP_SERVER_URL}/app/v2/suppliers`;
            const url = nextPage || `${baseUrl}?country=1&lang=en&ordering=-popularity&search=${search}&city=${city}`;
            const response: any = await axios.get(url);
            dispatch(addSuppliers(response.data.results));
            dispatch(setNextPageUrl((response.data.next) ? response.data.next : ''));
        } catch (error) {
            console.error('Failed to fetch suppliers:', error);
            // Handle error
        }
    }, [dispatch]);

    return { fetchSuppliers };
};
