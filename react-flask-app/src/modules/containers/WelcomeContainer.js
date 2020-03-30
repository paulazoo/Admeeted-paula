import React, { useEffect } from 'react';
import Welcome from '../views/Welcome';
import {loadData, changeData, resetNewUser} from "../actions";
import { connect } from 'react-redux';
import {Redirect, withRouter} from 'react-router-dom';

function WelcomeContainer ({ profile, currentlySending, setUser, loadProfile, setProfile }) {
    useEffect(() => {
        loadProfile();
        setUser();
    },[]);

    return (
        <div>
            <Welcome profile={profile} currentlySending={currentlySending} setProfile={setProfile}/>
        </div>
    )
}

const mapStateToProps = state => ({
    profile: state.data.profile,
    currentlySending: state.currentlySending,
})

const mapDispatchToProps = dispatch => ({
    setUser: () => {
        dispatch(resetNewUser(false))
    },
    loadProfile: () => {
        dispatch(loadData('/profile', 'profile'))
    },
    setProfile: (new_data) => {
        dispatch(changeData('/profile', new_data, ['/profile'], ['profile']))
    }
})

export default withRouter(connect(mapStateToProps, mapDispatchToProps)(WelcomeContainer))