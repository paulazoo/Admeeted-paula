import React, {useEffect} from 'react';
import Homepage from '../views/Homepage';
import { loadData } from "../actions";
import { connect } from 'react-redux';
import { withRouter } from 'react-router-dom';

function HomepageContainer ({ data, loadData }) {
    useEffect(() => {
        loadData();
    }, []);

    return (
        <Homepage data={data}/>
    )
}

const mapStateToProps = state => ({
    data: state.data.upcomingConvos,
})

const mapDispatchToProps = dispatch => ({
    loadData: () => dispatch(loadData('/upcoming-convos', 'upcomingConvos'))
})

export default withRouter(connect(mapStateToProps, mapDispatchToProps)(HomepageContainer))