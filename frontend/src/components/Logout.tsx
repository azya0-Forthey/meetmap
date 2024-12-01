import React, {useContext, useEffect} from 'react';
import {Context} from "../index";
import {useNavigate} from "react-router-dom";
import {observer} from "mobx-react-lite";

function Logout() {
    const {store} = useContext(Context);
    const navigate = useNavigate();

    useEffect(() => {
        store.logout().then(() => navigate("/"))
    }, []);

    return (
        <div></div>
    );
}

export default observer(Logout);