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
            console.log("setNextPageUrl: state", JSON.stringify(state));
        },
        addSuppliers(state, action: PayloadAction<Supplier[]>) {
            state.suppliers = [...state.suppliers, ...action.payload];
            console.log("addSuppliers: state", JSON.stringify(state));
        },
        clearSuppliers(state) {
            state.suppliers = [];
            console.log("addSuppliers: state", JSON.stringify(state));
        }
    },
});

export const { setNextPageUrl, addSuppliers, clearSuppliers } = suppliersSlice.actions;
export default suppliersSlice.reducer;
