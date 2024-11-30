import "../styles/LoginForm.css"

import React, {FC, useContext, useState} from 'react';
import {Context} from "../index";

function LoginForm() {
    const [username, setUsername] = useState<string>("");
    const [password, setPassword] = useState<string>("");
    const {store} = useContext(Context)

    return (
        <div className="login-form-container">
            <input
                onChange={e => setUsername(e.target.value)}
                value={username}
                type="text"
                placeholder="Имя пользователя"
            />
            <input
                onChange={e => setPassword(e.target.value)}
                value={password}
                type="password"
                placeholder="Пароль"
            />
            <button onClick={() => store.login(username, password)}>Войти</button>
        </div>
    );
};

export default LoginForm;