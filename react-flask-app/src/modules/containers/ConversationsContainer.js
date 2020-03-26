import React, { useEffect } from 'react';
import Conversations from '../views/Conversations';
import { loadData } from "../actions";
import { connect } from 'react-redux';
import { withRouter } from 'react-router-dom';

function ConversationsContainer ({ data, currentlySending, loadUpcomingConvos, loadAvailConvos }) {
    useEffect(() => {
        loadUpcomingConvos();
        loadAvailConvos();
    }, []);
    console.log(data);

    return (
        <Conversations data={data} currentlySending={currentlySending}/>
    )
}

const mapStateToProps = state => ({
    data: state.data,
    currentlySending: state.currentlySending,
})

const mapDispatchToProps = dispatch => ({
    loadUpcomingConvos: () => {
        dispatch(loadData('/upcoming-convos', 'upcomingConvos'));
    },
    loadAvailConvos: () => {
        dispatch(loadData('/avail-convos', 'availConvos'));
    },
})

export default withRouter(connect(mapStateToProps, mapDispatchToProps)(ConversationsContainer))