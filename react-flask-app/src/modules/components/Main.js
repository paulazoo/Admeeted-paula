import React from 'react';
import { Switch, Route } from 'react-router-dom';

import ProductHero from '../views/ProductHero';
import SignUp from '../views/SignUp';
import SignIn from '../views/SignIn';

const Main = () => {
  return (
    <Switch>
      <Route exact path='/' component={ProductHero}></Route>
      <Route exact path='/sign-up' component={SignUp}></Route>
      <Route exact path='/sign-in' component={SignIn}></Route>
    </Switch>
  );
}


export default Main;