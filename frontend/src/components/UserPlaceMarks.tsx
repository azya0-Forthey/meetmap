import React, {useCallback, useContext, useEffect} from 'react';
import {YMapDefaultMarker, YMapHint} from "../lib/ymaps";
import HintWindow from "./HintWindow";
import {LngLat} from "ymaps3";
import PLaceMarksService from "../services/PLaceMarksService";
import {Context} from "../index";
import {observer} from "mobx-react-lite"

function UserPlaceMarks() {
    const getHint = useCallback((object) => object?.properties?.hint, []);
    const [placeMarks, setPlaceMarks] = React.useState([]);
    const {store} = useContext(Context);

    useEffect(() => {
        if (!store.isAuth) {
            return;
        }

        PLaceMarksService.getUserPlaceMarks()
            .then(response => setPlaceMarks(response.data));
    }, [store.isAuth]);

    return (
        <>
            {/*@ts-ignore */}
            <YMapHint hint={getHint}>
                <HintWindow/>
            </YMapHint>
            {
                placeMarks.map((placeMark, index) => {
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
                    return <YMapDefaultMarker key={index} data-index={index} {...markerProps}/>
                })
            }
        </>
    );
}

export default observer(UserPlaceMarks);