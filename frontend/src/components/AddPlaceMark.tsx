import React from 'react';
import PLaceMarksService from "../services/PLaceMarksService";
import {useNavigate} from "react-router-dom";

function AddPlaceMark() {
    const [name, setName] = React.useState<string>("");
    const [description, setDescription] = React.useState<string>("");
    const [latitude, setLatitude] = React.useState<number>(37.588144);
    const [longitude, setLongitude] = React.useState<number>(55.733842);
    const navigator = useNavigate();

    function addPlaceMark() {
        PLaceMarksService.addPlaceMark({
            name: name,
            description: description,
            latitude: latitude,
            longitude: longitude
        }).then(response => {
            navigator("/")
        })
    }
    return (
        <div className="form">
            <h2>Добавление метки</h2>
            <input type="text" placeholder="Название" required
                   onChange={(e) => setName(e.target.value)}/>
            <input type="test" placeholder="Описание" required
                   onChange={(e) => setDescription(e.target.value)}/>
            <input type="number" placeholder="Широта (55.733842)" required
                   onChange={(e) => setLatitude(Number(e.target.value))}/>
            <input type="number" placeholder="Долгота (37.588144)" required
                   onChange={(e) => setLongitude(Number(e.target.value))}/>
            <button className="form-submit"
                    onClick={() => addPlaceMark()}>
                Добавить
            </button>
        </div>
    );
}

export default AddPlaceMark;