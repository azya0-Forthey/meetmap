import React, {useState} from "react";
import "../styles/NavigationBar.css";
import {Link} from "react-router-dom";

function NavigationBar() {
    const [isOpen, setIsOpen] = useState(false);

    return (
        <nav className="navbar">
            <ul>
                <li><Link to="/login">Войти</Link></li>
                <li>
                    <a href="#">Метки</a>
                    <ul>
                        <li><a href="#">Создать метку</a></li>
                        <li><a href="#">Список меток</a></li>
                    </ul>
                </li>
            </ul>
        </nav>
    );
}

export default NavigationBar;