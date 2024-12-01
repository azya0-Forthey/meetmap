import "../styles/HintWindow.css"

import {useContext, useEffect} from "react";
import {YMapHintContext} from "../lib/ymaps";

export default function HintWindow() {
    const hintContext = useContext(YMapHintContext) as {
        hint: {
            title: string
            text: string
            time: Date
        };
    };

    return (
        hintContext && (
            <div className="hint_window">
                <div className="hint_window__title">{hintContext.hint.title}</div>
                <div className="hint_window__text">{hintContext.hint.text}</div>
                <div className="hint_window__text">{new Intl.DateTimeFormat('ru-RU', {
                    year: 'numeric',
                    month: '2-digit',
                    day: '2-digit',
                    hour: '2-digit',
                    minute: '2-digit',
                    second: '2-digit'
                }).format(new Date(hintContext.hint.time))}</div>
            </div>
        )
    );
}