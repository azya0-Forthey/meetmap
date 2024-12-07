import {createContext} from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import Store from "./store/store";

const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);

const store = new Store();

export const Context = createContext<{store: Store}>({
    store,
});

root.render(
    <Context.Provider value={{store}}>
        <App />
    </Context.Provider>
);
