import React, {useEffect} from 'react';
import Homepage from '../views/Homepage';
import {loadData, new_loadData, resetNewUser} from "../actions";
import { connect } from 'react-redux';
import {Redirect, withRouter} from 'react-router-dom';

function HomepageContainer ({ newUser, data, currentlySending, setUser, loadAllData, loadUpcomingConvos, loadPastConvos, loadOrganizations }) {
    useEffect(() => {
        // loadAllData();
        loadUpcomingConvos();
        loadPastConvos();
        loadOrganizations();
    }, []);
    console.log(data);

    if (newUser) {
        return <Redirect to={'/welcome'}/>
    }

    return (
        <Homepage data={data} currentlySending={currentlySending}/>
    )
}

const mapStateToProps = state => ({
    newUser: state.newUser,
    data: state.data,
    currentlySending: state.currentlySending,
})

const mapDispatchToProps = dispatch => ({
    loadAllData: () => {
        dispatch(new_loadData(['/upcoming-events', '/past-conversations', '/organizations'],
            ['upcomingEvents', 'conversations', 'organizations']))
    },
    loadUpcomingConvos: () => {
        dispatch(loadData('/upcoming-events', 'upcomingEvents'));
    },
    loadPastConvos: () => {
        dispatch(loadData('/past-conversations', 'conversations'));
    },
    loadOrganizations: () => {
        dispatch(loadData('/organizations', 'organizations'));
    }
})

export default withRouter(connect(mapStateToProps, mapDispatchToProps)(HomepageContainer))