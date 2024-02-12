import { createSlice, PayloadAction } from '@reduxjs/toolkit';
import { Supplier, SuppliersResponse } from './types'; // Assuming types are defined

interface SupplierState {
    suppliers: Supplier[];
    loading: boolean;
    next: string | null;
    error: string | null;
}

const initialState: SupplierState = {
    suppliers: [],
    loading: false,
    next: null,
    error: null,
};

export const suppliersSlice = createSlice({
    name: 'suppliers',
    initialState,
    reducers: {
        setNextPageUrl(state, action: PayloadAction<string>) {
            state.next = action.payload;
        },
        addSuppliers(state, action: PayloadAction<Supplier[]>) {
            state.suppliers = [...state.suppliers, ...action.payload];
        },
    },
});

export const { setNextPageUrl, addSuppliers } = suppliersSlice.actions;
export default suppliersSlice.reducer;
