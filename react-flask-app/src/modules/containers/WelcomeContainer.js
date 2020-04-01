import React, {useEffect, useState} from 'react';
import Welcome from '../views/Welcome';
import {loadData, changeData, resetNewUser} from "../actions";
import { connect } from 'react-redux';
import {Redirect, withRouter} from 'react-router-dom';

function WelcomeContainer ({
    profile,
    allMajors,
    allOrganizations,
    currentlySending,
    setUser,
    loadProfile,
    loadMajors,
    setProfile,
    history
}) {
    useEffect(() => {
        loadProfile();
        loadMajors();
        setUser();
    },[]);

    return (
        <div>
            <Welcome
                profile={profile}
                allMajors={allMajors}
                allOrganizations={allOrganizations}
                currentlySending={currentlySending}
                setProfile={setProfile}
                history={history}
            />
        </div>
    )
}

const mapStateToProps = state => ({
    profile: state.data.profile,
    allMajors: state.data.allMajors,
    allOrganizations: state.data.allOrganizations,
    currentlySending: state.currentlySending,
})

const mapDispatchToProps = dispatch => ({
    setUser: () => {
        dispatch(resetNewUser(false))
    },
    loadProfile: () => {
        dispatch(loadData('/profile', 'profile'))
    },
    loadMajors: () => {
        dispatch(loadData('/majors', 'allMajors'))
    },
    setProfile: (new_data) => {
        dispatch(changeData('/profile', new_data, ['/profile'], ['profile']))
    },
    loadOrganizations: () => {
        dispatch(loadData('/all-organizations', 'allOrganizations'))
    }
})

export default withRouter(connect(mapStateToProps, mapDispatchToProps)(WelcomeContainer))