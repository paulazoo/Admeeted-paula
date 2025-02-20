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
import StaticGoogleLogin from "../views/StaticGoogleLogin";
import SearchBarContainer from "../containers/SearchBarContainer";
import WelcomeContainer from "../containers/WelcomeContainer";
import MasterContainer from "../containers/MasterContainer";
import ConvochatContainer from "../containers/ConvochatContainer";
import { connect } from 'react-redux';

function Main ({ loggedIn }) {
    const staticPage = false;
    if (staticPage) {
        return (
            <Switch>
                <Route exact path='/' component={ProductHero}/>
                <Route exact path='/sign-up' component={StaticGoogleForm}/>
            </Switch>
        )
    }

    return (
        <div>
            {
                loggedIn ? <Switch>
                    <Route exact path='/' component={HomepageContainer}/>
                    {/*<Route exact path='/sign-up' component={SignUp}/>*/}
                    {/*<Route exact path='/sign-in' component={SignInContainer}/>*/}
                    {/*<Route exact path='/sign-in' component={StaticGoogleLogin}/>*/}
                    {/*<Route exact path='/sign-out' component={SignOutContainer}/>*/}
                    <Route exact path='/events' component={EventsContainer}/>
                    <Route exact path='/account' component={AccountContainer}/>
                    <Route exact path='/welcome' component={WelcomeContainer}/>
                    {/*<Route exact path='/organizations' component={SearchBarContainer}/>*/}
                    <Route exact path={`/organization/:org_uid`} component={OrganizationContainer}/>
                    <Route exact path={'/master'} component={MasterContainer}/>
                    <Route exact path={`/convochat/:convo_uid`} component={ConvochatContainer}/>
                </Switch> : <Switch>
                    <Route path='/' component={ProductHero}/>
                </Switch>
            }
        </div>
    );
}

const mapStateToProps = state => ({
  loggedIn: state.loggedIn
})

export default connect(mapStateToProps, null)(Main);