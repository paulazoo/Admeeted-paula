import React, { useEffect } from 'react';
import Homepage from '../views/Homepage';
import { loadData } from "../actions";
import { connect } from 'react-redux';
import { withRouter } from 'react-router-dom';
import SearchBar from "../components/SearchBar";

function Container ({ all_organizations, currentlySending, loadOrganizations }) {
    useEffect(() => {
        loadOrganizations()
    },[])

    console.log(all_organizations)

    return <SearchBar all_organizations={all_organizations} currentlySending={currentlySending}/>
}

const mapStateToProps = state => ({
    all_organizations: state.data.allOrganizations,
    currentlySending: state.currentlySending,
})

const mapDispatchToProps = dispatch => ({
    loadOrganizations: () => {
        dispatch(loadData('/all_organizations', 'allOrganizations'))
    }
})

export default withRouter(connect(mapStateToProps, mapDispatchToProps)(Container))