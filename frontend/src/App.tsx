import "./App.css"

import Map from "./components/Map";
import {BrowserRouter, Route, Routes} from "react-router-dom";
import LoginForm from "./components/LoginForm";
import RegisterForm from "./components/RegisterForm";

export default function App() {
    return (
        <>
            <BrowserRouter>
            <Routes>
                <Route path="/" element={<Map />} />
                <Route path="/login" element={<LoginForm />} />
                <Route path="/register" element={<RegisterForm />} />
            </Routes>
            </BrowserRouter>
        </>
    );
}