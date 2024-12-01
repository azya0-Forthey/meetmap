import "../styles/RegisterLoginForm.css"

import React, {useContext, useEffect, useState} from "react";
import {Link, useNavigate} from "react-router-dom";
import {Context} from "../index";
import {observer} from "mobx-react-lite";

function RegisterLoginForm() {
    const [isLogin, setIsLogin] = useState(true);
    const {store} = useContext(Context);
    const navigate = useNavigate();

    useEffect(() => {
        if (store.isAuth) {
            navigate("/")
        }
    }, []);

    const toggleForm = () => {
        setIsLogin(!isLogin);
    };

    return (
        <div className="form-container">
            <div className="form-header">
                <button
                    className={`form-toggle ${isLogin ? "active" : ""}`}
                    onClick={() => setIsLogin(true)}
                >
                    Login
                </button>
                <button
                    className={`form-toggle ${!isLogin ? "active" : ""}`}
                    onClick={() => setIsLogin(false)}
                >
                    Register
                </button>
            </div>
            {isLogin ? <LoginForm/> : <RegisterForm/>}
            <button className="home-button">
                <Link to="/">На главную</Link>
            </button>
        </div>
    );
}

function LoginForm() {
    const [username, setUsername] = useState<string>("");
    const [password, setPassword] = useState<string>("");
    const [isValid, setIsValid] = useState<boolean>(true);
    const {store} = useContext(Context)
    const navigate = useNavigate();

    function login() {
        store.login(username, password).then(
            () => {store.isAuth ? navigate("/") : setIsValid(false)}
        )
    }

    return (
        <div className="form">
            <h2>Вход в аккаунт</h2>
            <input type="text" placeholder="Имя пользователя" required
                   onChange={(e) => setUsername(e.target.value)}/>
            <input type="password" placeholder="Пароль" required
                   onChange={(e) => setPassword(e.target.value)}/>
            <button className="form-submit"
                    onClick={() => login()}>
                Войти
            </button>
        </div>
    )
}

function RegisterForm() {
    const [username, setUsername] = useState<string>("");
    const [email, setEmail] = useState<string>("");
    const [password, setPassword] = useState<string>("");
    const [isValid, setIsValid] = useState<boolean>(true);
    const navigate = useNavigate();
    const {store} = useContext(Context)

    function register() {
        store.register(email, username, password).then(
            () => {store.isAuth ? navigate("/") : setIsValid(false)}
        )
    }

    return (
        <div className="form">
            <h2>Создание аккаунта</h2>
            <input type="text" placeholder="Имя пользователя" required
                   onChange={(e) => setUsername(e.target.value)}/>
            <input type="email" placeholder="Email" required
                   onChange={(e) => setEmail(e.target.value)}/>
            <input type="password" placeholder="Пароль" required
                   onChange={(e) => setPassword(e.target.value)}/>
            <button className="form-submit"
                    onClick={() => register()}>
                Регистрация
            </button>
        </div>
    )
}

export default observer(RegisterLoginForm);
