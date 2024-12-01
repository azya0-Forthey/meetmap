import {User} from "../models/response/User";
import {makeAutoObservable} from "mobx"
import AuthService from "../services/AuthService";
import axios from "axios";
import {AuthResponse} from "../models/response/AuthResponse";
import {API_URL} from "../http";

export default class Store {
    user = {} as User;
    isAuth = false;

    constructor() {
        makeAutoObservable(this);
    }

    setAuth(bool: boolean) {
        this.isAuth = bool;
    }

    setUser(user: User) {
        this.user = user;
    }

    async login(username: string, password: string) {
        try {
            const response = await AuthService.login({
                username: username,
                password: password
            });
            localStorage.setItem("token", response.data.access_token);
            this.setAuth(true)
            this.setUser((await AuthService.me()).data)
        } catch (e) {
            console.log(e.response?.data?.message);
        }
    }

    async register(email: string, username: string, password: string) {
        try {
            const response = await AuthService.register({
                email: email,
                username: username,
                password: password,
            });
            await this.login(username, password)
        } catch (e) {
            console.log(e.response?.data?.message);
        }
    }

    async logout() {
        try {
            await AuthService.logout();
            localStorage.removeItem("token");
            this.setAuth(false)
            this.setUser({} as User)
        } catch (e) {
            console.log(e.response?.data?.message);
        }
    }

    async checkAuth() {
        try {
            const response = await axios.get<AuthResponse>(`${API_URL}/users/refresh`, {withCredentials: true});
            localStorage.setItem("token", response.data.access_token);
            this.setAuth(true)
            this.setUser((await AuthService.me()).data)
        } catch (e) {
            console.log(e.response?.data?.message);
        }
    }
}