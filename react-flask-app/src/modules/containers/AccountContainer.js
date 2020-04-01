import React, { useEffect } from 'react';
import Account from '../views/Account';
import { loadData, changeData } from "../actions";
import { connect } from 'react-redux';
import { withRouter } from 'react-router-dom';

function AccountContainer ({ profile, allMajors, allInterests, currentlySending, loadProfile, loadMajors, loadInterests, setProfile }) {
    useEffect(() => {
        loadProfile();
        loadMajors();
        loadInterests();
    },[]);

    return (
        <Account
            profile={profile}
            allMajors={allMajors}
            allInterests={allInterests}
            currentlySending={currentlySending}
            setProfile={setProfile}
        />
    )
}

const mapStateToProps = state => ({
    profile: state.data.profile,
    allMajors: state.data.allMajors,
    allInterests: state.data.allInterests,
    currentlySending: state.currentlySending,
})

const mapDispatchToProps = dispatch => ({
    loadProfile: () => {
        dispatch(loadData('/profile', 'profile'))
    },
    loadMajors: () => {
        dispatch(loadData('/majors', 'allMajors'))
    },
    loadInterests: () => {
        dispatch(loadData('/interests', 'allInterests'))
    },
    setProfile: (new_data) => {
        dispatch(changeData('/profile', new_data, ['/profile'], ['profile']))
    }
})

export default withRouter(connect(mapStateToProps, mapDispatchToProps)(AccountContainer))