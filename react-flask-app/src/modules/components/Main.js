import React from 'react';
import { Switch, Route } from 'react-router-dom';

import ProductHero from '../views/ProductHero';
import HomepageContainer from '../containers/HomepageContainer';
import Conversations from '../views/Events';
import SignUp from '../views/SignUp';
import SignInContainer from '../containers/SignInContainer';
import StaticGoogleForm from "../views/StaticGoogleForm";
import SignOutContainer from "../containers/SignOutContainer";
import EventsContainer from "../containers/EventsContainer";
import AccountContainer from "../containers/AccountContainer";
import OrganizationContainer from "../containers/OrganizationContainer";

const Main = () => {
    const staticPage = false;
    return (
        <div>
            {!staticPage ? <Switch>
                <Route exact path='/' component={ProductHero}/>
                <Route exact path='/home' component={HomepageContainer}/>
                <Route exact path='/sign-up' component={SignUp}/>
                <Route exact path='/sign-in' component={SignInContainer}/>
                <Route exact path='/sign-out' component={SignOutContainer}/>
                <Route exact path='/events' component={EventsContainer}/>
                <Route exact path='/account' component={AccountContainer}/>
                <Route exact path={`/organization/:org_uid`} component={OrganizationContainer}/>
            </Switch> : <Switch>
                <Route exact path='/' component={ProductHero}/>
                <Route exact path='/sign-up' component={StaticGoogleForm}/>
            </Switch>}
        </div>
    );
}


export default Main;