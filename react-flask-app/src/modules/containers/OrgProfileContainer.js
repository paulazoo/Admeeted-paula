import React, { useEffect } from 'react';
import Organization from '../views/Organization';
import { loadData, loadOrgData } from "../actions";
import { connect } from 'react-redux';
import { withRouter } from 'react-router-dom';

function OrgProfileContainer ({
    match,
    profile,
    currentlySending,
    loadOrgProfile
}) {
    const org_uid = match.params.org_uid;

    useEffect(() => {
        loadOrgProfile(org_uid);
    },[]);

    console.log(profile);

    return (
        <Organization profile={profile} org_uid={org_uid} currentlySending={currentlySending}/>
    )
}

const mapStateToProps = state => ({
    profile: state.org_data.profile,
    currentlySending: state.currentlySending
})

const mapDispatchToProps = dispatch => ({
    loadOrgProfile: (org_uid) => {
        dispatch(loadOrgData(`/organizations-old/${org_uid}`, 'profile'))
    }
})

export default withRouter(connect(mapStateToProps, mapDispatchToProps)(OrgProfileContainer))