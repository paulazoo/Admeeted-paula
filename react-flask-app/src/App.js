import withRoot from './modules/withRoot';
import React, { useState, useEffect } from 'react';
import { connect } from 'react-redux';
import logo from './logo.svg';
import './App.css';
import AppAppBar from './modules/views/AppAppBar';
import AppFooter from './modules/views/AppFooter';
import Main from './modules/components/Main';
import StaticGoogleForm from './modules/views/StaticGoogleForm';
import {loadMe} from "./modules/actions";

function App({ loadUser }) {
  const [currTime, setCurrTime] = useState(0);

  useEffect(() => {
    fetch('/time').then(res => res.json()).then(data => {
      setCurrTime(data.time);
    });
  }, []);

  useEffect(() => {
      loadUser();
  }, []);

  return (
      <React.Fragment>
          <AppAppBar/>
          {/*<StaticGoogleForm/>*/}
          <Main/>
          <AppFooter/>
      </React.Fragment>
  );
}

const mapDispatchToProps = dispatch => ({
    loadUser: () => dispatch(loadMe())
});

export default withRoot(connect(null, mapDispatchToProps)(App));
