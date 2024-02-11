import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import API from '../services/api';

interface SupplierState {
  suppliers: any[];
  loading: boolean;
}

const initialState: SupplierState = {
  suppliers: [],
  loading: false,
};

export const fetchSuppliers = createAsyncThunk('suppliers/fetchSuppliers', async (params: string) => {
  const response = await API.get(`/app/v2/suppliers${params}`);
  return response.data;
});

const suppliersSlice = createSlice({
  name: 'suppliers',
  initialState,
  reducers: {},
  extraReducers: (builder) => {
    builder.addCase(fetchSuppliers.pending, (state) => {
      state.loading = true;
    });
    builder.addCase(fetchSuppliers.fulfilled, (state, action) => {
      state.suppliers = action.payload.results;
      state.loading = false;
    });
    builder.addCase(fetchSuppliers.rejected, (state) => {
      state.loading = false;
    });
  },
});

export default suppliersSlice.reducer;
