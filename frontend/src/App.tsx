import "./App.css"
import {
    YMap,
    YMapDefaultSchemeLayer,
    YMapDefaultFeaturesLayer,
    YMapDefaultMarker, YMapHint, YMapHintContext,
} from './lib/ymaps';
import useWindowDimensions from "./lib/get_window_size";
import {useCallback, useContext, useEffect, useState} from "react";
import {LngLat, YMapLocationRequest} from "ymaps3";
import HintWindow from "./components/HintWindow";

interface PlaceMark {
    "name": string
    "description": string
    "latitude": number
    "longitude": number
    "id": number
    "create_date": Date
    "is_active": boolean
    "user_id": number
}

export default function App() {
    const getHint = useCallback((object) => object?.properties?.hint, []);
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
            <YMap location={defaultLoc}>
                <YMapDefaultSchemeLayer/>
                <YMapDefaultFeaturesLayer/>

                 {/*@ts-ignore */}
                <YMapHint hint={getHint}>
                    <HintWindow/>
                </YMapHint>
                {
                    markerSource.map((placeMark, index) => {
                        const markerProps = {
                            coordinates: [placeMark.latitude, placeMark.longitude] as LngLat,
                            title: placeMark.name,
                            subtitle: placeMark.description,
                            color: 'lavender',
                            size: 'normal',
                            iconName: 'fallback',
                            properties: {
                                hint: {
                                    title: placeMark.name,
                                    text: placeMark.description,
                                    time: placeMark.create_date
                                }
                            }
                        }
                        // @ts-ignore
                        return <YMapDefaultMarker key={index} data-index={index} {...markerProps}
                                                  onClick={() => alertInfo(index)}/>
                    })
                }
            </YMap>
        </div>
    );
}