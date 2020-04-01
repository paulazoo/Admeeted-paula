import React, { useEffect } from 'react';
import Homepage from '../views/Homepage';
import { loadData, genConvos, genEmptyHangouts } from "../actions";
import { connect } from 'react-redux';
import { withRouter } from 'react-router-dom';
import Button from '@material-ui/core/Button';
import MainLayout from "../layouts/MainLayout";
import Master from "../views/Master";

function MasterContainer ({ events, currentlySending, loadUpcomingConvos, generateConvos, generateEmptyHangouts }) {
    useEffect(() => {
        loadUpcomingConvos();
    },[])

    console.log(events);

    return (
        <Master
            events={events}
            currentlySending={currentlySending}
            generateConvos={generateConvos}
            generateEmptyHangouts={generateEmptyHangouts}
        />
    )
}

const mapStateToProps = state => ({
    events: state.data.upcomingEvents,
    currentlySending: state.currentlySending
})

const mapDispatchToProps = dispatch => ({
    loadUpcomingConvos: () => {
        dispatch(loadData('/upcoming-events', 'upcomingEvents'));
    },
    generateConvos: (event_uid, convo_name) => {
        dispatch(genConvos(event_uid, convo_name))
    },
    generateEmptyHangouts: (name, num_hangouts, num_threads) => {
        dispatch(genEmptyHangouts(name, num_hangouts, num_threads))
    }
})

export default withRouter(connect(mapStateToProps, mapDispatchToProps)(MasterContainer))