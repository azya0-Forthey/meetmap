import React, {useContext, useState} from "react";
import "../styles/NavigationBar.css";
import {Link} from "react-router-dom";
import {Context} from "../index";
import {observer} from "mobx-react-lite"

function NavigationBar() {
    const [isOpen, setIsOpen] = useState(false);
    const {store} = useContext(Context)

    return (
        <nav className="navbar">
            <ul>
                <li>{
                    store.isAuth
                        ?
                        <Link to="/logout">Выйти</Link>
                        :
                        <Link to="/login">Войти</Link>
                }</li>
                <li>
                    <a href="#">Метки</a>
                    <ul>
                        <li><a href="/placemark">Создать метку</a></li>
                        {/*<li><a href="#">Список меток</a></li>*/}
                    </ul>
                </li>
            </ul>
        </nav>
    );
}

export default observer(NavigationBar);