import React, { useEffect } from 'react';
import Account from '../views/Account';
import { loadData, changeData } from "../actions";
import { connect } from 'react-redux';
import { withRouter } from 'react-router-dom';

function AccountContainer ({ profile, currentlySending, loadProfile, setProfile }) {
    useEffect(() => {
        loadProfile();
    },[]);

    return (
        <Account profile={profile} currentlySending={currentlySending} setProfile={setProfile}/>
    )
}

const mapStateToProps = state => ({
    profile: state.data.profile,
    currentlySending: state.currentlySending,
})

const mapDispatchToProps = dispatch => ({
    loadProfile: () => {
        dispatch(loadData('/profile', 'profile'))
    },
    setProfile: (new_data) => {
        dispatch(changeData('/profile', new_data, ['/profile'], ['profile']))
    }
})

export default withRouter(connect(mapStateToProps, mapDispatchToProps)(AccountContainer))