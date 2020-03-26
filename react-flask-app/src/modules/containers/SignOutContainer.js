import React, { useEffect } from 'react';
import { connect } from 'react-redux';
import { withRouter, Redirect } from 'react-router-dom';
import { logout } from '../actions';
import Loading from "../views/Loading";

function SignOutContainer ({ loggedIn, handleLogout }) {
    useEffect(() => {
        if (loggedIn) {
            handleLogout();
        }
    }, []);

    return (
        <div>
            {!loggedIn ? <Redirect to="/"/> : <Loading/>}
        </div>
    )

}

const mapStateToProps = state => ({
    loggedIn: state.loggedIn,
})

const mapDispatchToProps = dispatch => ({
    handleLogout: () => dispatch(logout())
})

export default withRouter(connect(mapStateToProps, mapDispatchToProps)(SignOutContainer))