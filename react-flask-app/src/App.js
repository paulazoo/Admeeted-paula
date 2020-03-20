import withRoot from './modules/withRoot';
import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';
import AppAppBar from './modules/views/AppAppBar';
import AppFooter from "./modules/views/AppFooter";

function App() {
  const [currTime, setCurrTime] = useState(0);

  useEffect(() => {
    fetch('/time').then(res => res.json()).then(data => {
      setCurrTime(data.time);
    });
  }, []);

  return (
    <div className="App">
      <AppAppBar />
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
        <p>The current time is {currTime}</p>
      </header>
      <AppFooter />
    </div>
  );
}

export default withRoot(App);
