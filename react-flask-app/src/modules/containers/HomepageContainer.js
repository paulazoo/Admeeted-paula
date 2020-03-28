import React, {useEffect} from 'react';
import Homepage from '../views/Homepage';
import { loadData } from "../actions";
import { connect } from 'react-redux';
import { withRouter } from 'react-router-dom';

function HomepageContainer ({ data, currentlySending, loadUpcomingConvos, loadPastConvos, loadOrganizations }) {
    useEffect(() => {
        loadUpcomingConvos();
        loadPastConvos();
        loadOrganizations();
    }, []);
    console.log(data);

    return (
        <Homepage data={data} currentlySending={currentlySending}/>
    )
}

const mapStateToProps = state => ({
    data: state.data,
    currentlySending: state.currentlySending,
})

const mapDispatchToProps = dispatch => ({
    loadUpcomingConvos: () => {
        dispatch(loadData('/upcoming-convos', 'upcomingEvents'));
    },
    loadPastConvos: () => {
        dispatch(loadData('/past-convos', 'conversations'));
    },
    loadOrganizations: () => {
        dispatch(loadData('/organizations-old', 'organizations'));
    }
})

export default withRouter(connect(mapStateToProps, mapDispatchToProps)(HomepageContainer))