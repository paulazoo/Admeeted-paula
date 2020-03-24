import React from 'react';
import { Switch, Route } from 'react-router-dom';

import ProductHero from '../views/ProductHero';
import HomepageContainer from '../containers/HomepageContainer';
import Conversations from '../views/Conversations';
import SignUp from '../views/SignUp';
import SignInContainer from '../containers/SignInContainer';
import StaticGoogleForm from "../views/StaticGoogleForm";

const Main = () => {
    const staticPage = true;
    return (
        <div>
            {!staticPage ? <Switch>
                <Route exact path='/' component={ProductHero}/>
                <Route exact path='/home' component={HomepageContainer}/>
                <Route exact path='/sign-up' component={SignUp}/>
                <Route exact path='/sign-in' component={SignInContainer}/>
            </Switch> : <Switch>
                <Route exact path='/' component={ProductHero}/>
                <Route exact path='/sign-up' component={StaticGoogleForm}/>
            </Switch>}
        </div>
    );
}


export default Main;