import React, {MouseEventHandler, useCallback, useEffect, useState} from 'react';
import {Config, DomEventHandlerObject, LngLat, MapEventUpdateHandler, YMapLocationRequest} from "ymaps3";
import useWindowDimensions from "../lib/get_window_size";
import {
    YMap,
    YMapDefaultFeaturesLayer,
    YMapDefaultMarker,
    YMapDefaultSchemeLayer,
    YMapHint,
    YMapListener
} from "../lib/ymaps";
import HintWindow from "./HintWindow";
import NavigationBar from "./NavigationBar";
import UserPlaceMarks from "./UserPlaceMarks";

function Map() {
    const [markerSource, setMarkerSource] = useState<PlaceMark[]>([])

    useEffect(() => {
        setMarkerSource([{
            name: 'ЭТО МОСКВА',
            description: 'И Я НАКОНЕЦ-ТО ЗАСТАВИЛ ЭТУ ВЕЩЬ РАБОТАТЬ',
            latitude: 37.588144,
            longitude: 55.733842,
            id: 1,
            create_date: new Date(),
            is_active: true,
            user_id: 1,
        }])
    }, [])

    const defaultLoc: YMapLocationRequest = {
        center: [37.588144, 55.733842],
        zoom: 9
    }

    function alertInfo(index: number) {
        alert(markerSource[index].description)
    }

    return (
        <div style={useWindowDimensions()}>
            <NavigationBar />
            <YMap location={defaultLoc} theme="dark">
                <YMapDefaultSchemeLayer/>
                <YMapDefaultFeaturesLayer/>
                <UserPlaceMarks/>
            </YMap>
        </div>
    );
}

export default Map;