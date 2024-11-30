import $api from "../http";
import {AxiosResponse} from "axios";
import {AuthResponse} from "../models/response/AuthResponse";
import {UserLoginRequest} from "../models/request/UserLoginRequest";
import {UserRegisterRequest} from "../models/request/UserRegisterRequest";
import {User} from "../models/response/User";

export default class AuthService {
    static async login(userLoginData: UserLoginRequest): Promise<AxiosResponse<AuthResponse>> {
        return $api.post<AuthResponse>("/users/login", userLoginData)
    }

    static async register(userRegisterData: UserRegisterRequest): Promise<AxiosResponse<number>> {
        return $api.post<number>("/users/register", userRegisterData)
    }

    static async logout(): Promise<void> {
        return $api.post("/logout")
    }

    static async me(): Promise<AxiosResponse<User>> {
        return $api.get<User>("/users/me")
    }
}