import { createSlice, PayloadAction } from '@reduxjs/toolkit';
import { Supplier, SuppliersResponse } from './types'; // Assuming types are defined

interface SupplierState {
    suppliers: Supplier[];
    loading: boolean;
    next: string | null;
    error: string | null;
    hasMore: boolean;
}

const initialState: SupplierState = {
    suppliers: [],
    loading: false,
    hasMore: true,
    next: null,
    error: null,
};

export const suppliersSlice = createSlice({
    name: 'suppliers',
    initialState,
    reducers: {
        setNextPageUrl(state, action: PayloadAction<string|null>) {
            state.next = action.payload
            state.hasMore = action.payload !== null
        },
        addSuppliers(state, action: PayloadAction<Supplier[]>) {
            state.suppliers = [...state.suppliers, ...action.payload];
        },
    },
});

export const { setNextPageUrl, addSuppliers } = suppliersSlice.actions;
export default suppliersSlice.reducer;
