import React, { useEffect } from 'react';
import Homepage from '../views/Homepage';
import { loadData, genConvos } from "../actions";
import { connect } from 'react-redux';
import { withRouter } from 'react-router-dom';
import Button from '@material-ui/core/Button';

function MasterContainer ({ events, loadUpcomingConvos, generateConvos }) {
    useEffect(() => {
        loadUpcomingConvos();
    },[])

    console.log(events);

    const convo_name = "Yale Sucks";

    const handleSubmit = event => {
        if (events.length > 0) {
            generateConvos(events[0].id, convo_name);
        }
    };

    return (<Button onClick={handleSubmit}>Click Me!</Button>)
}

const mapStateToProps = state => ({
    events: state.data.upcomingEvents
})

const mapDispatchToProps = dispatch => ({
    loadUpcomingConvos: () => {
        dispatch(loadData('/upcoming-events', 'upcomingEvents'));
    },
    generateConvos: (event_uid, convo_name) => {
        dispatch(genConvos(event_uid, convo_name))
    }
})

export default withRouter(connect(mapStateToProps, mapDispatchToProps)(MasterContainer))