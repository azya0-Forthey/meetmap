import axios from "axios";
import {AuthResponse} from "../models/response/AuthResponse";
import AuthService from "../services/AuthService";

export const API_URL = `http://localhost:443`

const $api = axios.create({
    withCredentials: true,
    baseURL: API_URL,
})

$api.interceptors.request.use((config) => {
    config.headers.Authorization = `Bearer ${localStorage.getItem("token")}`
    return config;
})

$api.interceptors.response.use((config) => {
    return config;
}, async (error) => {
    const originalRequest = error.config;
    if (error.response && error.response.status === 401 && error.config && !error.config._isRetry) {
        originalRequest._isRetry = true;
        try {
            const response = await axios.get<AuthResponse>(`${API_URL}/users/refresh`, {withCredentials: true});
            localStorage.setItem("token", response.data.access_token);
            return $api.request(originalRequest)
        } catch (error) {
            console.log(error.response?.data?.message);
        }
    }
    throw error;
})

export default $api;