import axios from 'axios';

const API = axios.create({
  baseURL: process.env.REACT_APP_SERVER_URL,
});

export default API;
