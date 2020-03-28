import React, { useEffect } from 'react';
import Homepage from '../views/Homepage';
import {loadData, loadOrgData} from "../actions";
import { connect } from 'react-redux';
import { withRouter } from 'react-router-dom';
import OrgDashboard from "../components/OrgDashboard";

function OrgDashboardContainer ({
    org_uid,
    upcomingEvents,
    availEvents,
    conversations,
    loadOrgUpcomingEvents,
    loadOrgAvailEvents,
    loadOrgConversations
}) {
    useEffect(() => {
        loadOrgUpcomingEvents(org_uid);
        loadOrgAvailEvents(org_uid);
        loadOrgConversations(org_uid);
    },[]);

    return (
        <OrgDashboard upcomingEvents={upcomingEvents} availEvents={availEvents} conversations={conversations}/>
    )
}

const mapStateToProps = state => ({
    upcomingEvents: state.org_data.upcomingEvents,
    availEvents: state.org_data.availEvents,
    conversations: state.org_data.conversations
})

const mapDispatchToProps = dispatch => ({
    loadOrgUpcomingEvents: (org_uid) => {
        dispatch(loadOrgData(`/upcoming-convos/${org_uid}`, 'upcomingEvents'))
    },
    loadOrgAvailEvents: (org_uid) => {
        dispatch(loadOrgData(`/avail-convos/${org_uid}`, 'availEvents'))
    },
    loadOrgConversations: (org_uid) => {
        dispatch(loadOrgData(`/past-convos/${org_uid}`, 'conversations'))
    }
})

export default withRouter(connect(mapStateToProps, mapDispatchToProps)(OrgDashboardContainer))