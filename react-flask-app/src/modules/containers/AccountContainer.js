import React, { useEffect } from 'react';
import Account from '../views/Account';
import { loadData } from "../actions";
import { connect } from 'react-redux';
import { withRouter } from 'react-router-dom';

function AccountContainer ({ profile, currentlySending, loadProfile }) {
    useEffect(() => {
        loadProfile();
    },[]);

    return (
        <Account profile={profile} currentlySending={currentlySending}/>
    )
}

const mapStateToProps = state => ({
    profile: state.data.profile,
    currentlySending: state.currentlySending,
})

const mapDispatchToProps = dispatch => ({
    loadProfile: () => {
        dispatch(loadData('/profile-old', 'profile'))
    }
})

export default withRouter(connect(mapStateToProps, mapDispatchToProps)(AccountContainer))