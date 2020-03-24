import withRoot from './modules/withRoot';
import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';
import AppAppBar from './modules/views/AppAppBar';
import AppFooter from './modules/views/AppFooter';
import Main from './modules/components/Main';

function App() {
  const [currTime, setCurrTime] = useState(0);

  useEffect(() => {
    fetch('/time').then(res => res.json()).then(data => {
      setCurrTime(data.time);
    });
  }, []);

  useEffect(() => {
      // loadUser();
  }, []);

  return (
      <React.Fragment>
          <AppAppBar/>
          <Main/>
          <AppFooter/>
      </React.Fragment>
  );
}

export default withRoot(App);
