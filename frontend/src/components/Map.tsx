import {YMapLocationRequest} from "ymaps3";
import useWindowDimensions from "../lib/get_window_size";
import {YMap, YMapDefaultFeaturesLayer, YMapDefaultSchemeLayer} from "../lib/ymaps";
import NavigationBar from "./NavigationBar";
import UserPlaceMarks from "./UserPlaceMarks";
import type {LngLatBounds, ZoomRange} from '@yandex/ymaps3-types';


function Map() {
    const defaultLoc: YMapLocationRequest = {
        center: [37.588144, 55.733842],
        zoom: 9
    }

    const RESTRICT_AREA: LngLatBounds = [
        [23.530451, 42.11191],
        [170.36641, 76.1558141]
    ];

    const ZOOM_AREA: ZoomRange = {
        min: 5,
        max: 20
    };

    return (
        <div style={useWindowDimensions()}>
            <NavigationBar />
            <YMap location={defaultLoc} restrictMapArea={RESTRICT_AREA} zoomRange={ZOOM_AREA} theme="dark">
                <YMapDefaultSchemeLayer/>
                <YMapDefaultFeaturesLayer/>
                <UserPlaceMarks/>
            </YMap>
        </div>
    );
}

export default Map;