import "./App.css"

import Map from "./components/Map";
import {BrowserRouter, Route, Routes} from "react-router-dom";
import RegisterLoginForm from "./components/RegisterLoginForm";
import {useContext, useEffect} from "react";
import {Context} from "./index";

export default function App() {
    const {store} = useContext(Context)
    useEffect(() => {
        store.checkAuth()
    }, [])

    return (
        <>
            <BrowserRouter>
            <Routes>
                <Route path="/" element={<Map />} />
                <Route path="/login" element={<RegisterLoginForm />} />
            </Routes>
            </BrowserRouter>
        </>
    );
}