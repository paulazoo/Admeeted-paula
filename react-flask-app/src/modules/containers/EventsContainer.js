import React, { useEffect } from 'react';
import Events from '../views/Events';
import { loadData, changeData } from "../actions";
import { connect } from 'react-redux';
import { withRouter } from 'react-router-dom';

function EventsContainer ({ data, currentlySending, loadUpcomingEvents, loadAvailEvents, modifyEvent }) {
    useEffect(() => {
        loadUpcomingEvents();
        loadAvailEvents();
    }, []);
    console.log(data);

    return (
        <Events data={data} currentlySending={currentlySending} modifyEvent={modifyEvent}/>
    )
}

const mapStateToProps = state => ({
    data: state.data,
    currentlySending: state.currentlySending,
})

const mapDispatchToProps = dispatch => ({
    loadUpcomingEvents: () => {
        dispatch(loadData('/upcoming-events', 'upcomingEvents'));
    },
    loadAvailEvents: () => {
        dispatch(loadData('/avail-events', 'availEvents'));
    },
    modifyEvent: (event_uid, signUp) => {
        dispatch(changeData(
            `/events/${event_uid}`,
            signUp,
            ['/upcoming-events', '/avail-events'],
            ['upcomingEvents', 'availEvents'])
        );
    }
})

export default withRouter(connect(mapStateToProps, mapDispatchToProps)(EventsContainer))