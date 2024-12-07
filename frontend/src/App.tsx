import "./App.css"

import Map from "./components/Map";
import {BrowserRouter, Route, Routes} from "react-router-dom";
import {observer} from "mobx-react-lite";
import RegisterLoginForm from "./components/RegisterLoginForm";
import {useContext, useEffect} from "react";
import {Context} from "./index";
import AddPlaceMark from "./components/AddPlaceMark";
import Logout from "./components/Logout";

function App() {
    const {store} = useContext(Context);

    useEffect(() => {
        if (localStorage.getItem("token")) {
            store.checkAuth()
        }
    }, [])

    return (
        <>
            <BrowserRouter>
                <Routes>
                    <Route path="/" element={<Map/>}/>
                    <Route path="/login" element={<RegisterLoginForm/>}/>
                    <Route path="/logout" element={<Logout/>}/>
                    <Route path="/placemark" element={<AddPlaceMark/>}/>
                </Routes>
            </BrowserRouter>
        </>
    );
}

export default observer(App);