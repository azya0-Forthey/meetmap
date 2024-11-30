import React, {FC, useContext, useState} from 'react';
import {Context} from "../index";

function RegisterForm() {
    const [email, setEmail] = useState<string>("");
    const [username, setUsername] = useState<string>("");
    const [password, setPassword] = useState<string>("");
    const {store} = useContext(Context)

    return (
        <div>
            <input
                onChange={e => setEmail(e.target.value)}
                value={email}
                type="text"
                placeholder="Почта"
            />
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
            <button onClick={() => store.register(email, username, password)}>Регистрация</button>
        </div>
    );
};

export default RegisterForm;