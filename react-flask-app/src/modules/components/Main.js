import React from 'react';
import { Switch, Route } from 'react-router-dom';

import ProductHero from '../views/ProductHero';
import Homepage from '../views/Homepage';
import Conversations from '../views/Conversations';
import SignUp from '../views/SignUp';
import SignInContainer from '../containers/SignInContainer';

const Main = () => {
    return (
        <Switch>
            <Route exact path='/' component={ProductHero}/>
            <Route exact path='/home' component={Homepage}/>
            <Route exact path='/sign-up' component={SignUp}/>
            <Route exact path='/sign-in' component={SignInContainer}/>
        </Switch>
    );
}


export default Main;