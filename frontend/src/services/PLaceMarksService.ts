import {AxiosResponse} from "axios";
import $api from "../http";
import PlaceMark from "../models/response/PlaceMark";

export default class PLaceMarksService {
    static async getUserPlaceMarks(): Promise<AxiosResponse<PlaceMark[]>> {
        try {
            return await $api.get<PlaceMark[]>("/placemarks")
        } catch (error) {
            console.log(error);
        }
    }

    static async addPlaceMark(placeMark: PlaceMarkAddRequest): Promise<AxiosResponse<number>> {
        try {
            return await $api.post<number>("/placemarks", placeMark)
        } catch (error) {
            console.log(error)
        }
    }
}