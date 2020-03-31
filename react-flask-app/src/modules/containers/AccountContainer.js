import React, { useEffect } from 'react';
import Account from '../views/Account';
import { loadData, changeData } from "../actions";
import { connect } from 'react-redux';
import { withRouter } from 'react-router-dom';

function AccountContainer ({ profile, allMajors, currentlySending, loadProfile, loadMajors, setProfile }) {
    useEffect(() => {
        loadProfile();
        loadMajors();
    },[]);

    return (
        <Account
            profile={profile}
            allMajors={allMajors}
            currentlySending={currentlySending}
            setProfile={setProfile}
        />
    )
}

const mapStateToProps = state => ({
    profile: state.data.profile,
    allMajors: state.data.allMajors,
    currentlySending: state.currentlySending,
})

const mapDispatchToProps = dispatch => ({
    loadProfile: () => {
        dispatch(loadData('/profile', 'profile'))
    },
    loadMajors: () => {
        dispatch(loadData('/majors', 'allMajors'))
    },
    setProfile: (new_data) => {
        dispatch(changeData('/profile', new_data, ['/profile'], ['profile']))
    }
})

export default withRouter(connect(mapStateToProps, mapDispatchToProps)(AccountContainer))