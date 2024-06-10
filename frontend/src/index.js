import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import { StateProvider } from './state/StateProvider';
import { initialstate, reducer } from './state/reducer';



const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <StateProvider reducer={reducer} initialstate={initialstate}>
        <App />
    </StateProvider>
);

