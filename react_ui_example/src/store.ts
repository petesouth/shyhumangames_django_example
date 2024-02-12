import { configureStore } from '@reduxjs/toolkit';
import suppliersReducer from './features/suppliersSlice';

export const store = configureStore({
    reducer: {
        suppliers: suppliersReducer,
    },
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
