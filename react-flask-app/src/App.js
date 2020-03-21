import withRoot from './modules/withRoot';
import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';
import AppAppBar from './modules/views/AppAppBar';
import AppFooter from './modules/views/AppFooter';
import ProductHero from './modules/views/ProductHero';

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
        <ProductHero />
      <AppFooter />
    </div>
  );
}

export default withRoot(App);
