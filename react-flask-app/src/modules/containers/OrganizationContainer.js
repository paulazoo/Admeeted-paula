import {changeOrgData, loadOrgData} from "../actions";
import {withRouter} from "react-router-dom";
import {connect} from "react-redux";
import React, {useEffect} from "react";
import Organization from "../views/Organization";

function OrganizationContainer ({
    match,
    org_data,
    currentlySending,
    loadOrgProfile,
    loadOrgUpcomingEvents,
    loadOrgAvailEvents,
    loadOrgConversations,
    modifyEvent
}) {
    const org_uid = match.params.org_uid;

    useEffect(() => {
        loadOrgProfile(org_uid);
        loadOrgUpcomingEvents(org_uid);
        loadOrgAvailEvents(org_uid);
        loadOrgConversations(org_uid);
    },[]);

    console.log(org_data);

    return (
        <Organization org_data={org_data} org_uid={org_uid} currentlySending={currentlySending} modifyEvent={modifyEvent}/>
    )
}

const mapStateToProps = state => ({
    org_data: state.org_data,
    currentlySending: state.currentlySending
})

const mapDispatchToProps = dispatch => ({
    loadOrgProfile: (org_uid) => {
        dispatch(loadOrgData(`/organizations/${org_uid}`, 'profile'))
    },
    loadOrgUpcomingEvents: (org_uid) => {
        dispatch(loadOrgData(`/upcoming-events/${org_uid}`, 'upcomingEvents'))
    },
    loadOrgAvailEvents: (org_uid) => {
        dispatch(loadOrgData(`/avail-events/${org_uid}`, 'availEvents'))
    },
    loadOrgConversations: (org_uid) => {
        dispatch(loadOrgData(`/conversations-NOT-READY/${org_uid}`, 'conversations'))
    },
    modifyEvent: (event_uid, signUp, org_uid) => {
        dispatch(changeOrgData(
            `/events/${event_uid}`,
            signUp,
            [`/upcoming-events/${org_uid}`, `/avail-events/${org_uid}`],
            ['upcomingEvents', 'availEvents'])
        );
    }
})

export default withRouter(connect(mapStateToProps, mapDispatchToProps)(OrganizationContainer))