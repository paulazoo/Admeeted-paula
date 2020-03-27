import React, {useEffect} from 'react';
import { connect } from 'react-redux';
import { withRouter, Redirect } from 'react-router-dom';

import SignIn from '../views/SignIn';
import { login, setErrorMessage } from "../actions";

function SignInContainer ({ loggedIn, handleSubmit, errorMessage }) {
    // THIS CODE REPLACES THE ACTUAL FORM PAGE
    useEffect(() => {
        if (!loggedIn) {
            handleSubmit('a', 'b')
        }
    }, []);

    return (
        <div>
            {loggedIn ? (
                <Redirect to='/' />
            ) : (
                <SignIn
                    handleSubmit={handleSubmit}
                    errorMessage={errorMessage}
                />
            )}
        </div>
    );
}

const mapStateToProps = state => ({
    loggedIn: state.loggedIn,
    errorMessage: state.errorMessage
})

const mapDispatchToProps = dispatch => ({
    handleSubmit: (username, password) => dispatch(login(username, password)),
    clearErrors: () => dispatch(setErrorMessage(''))
})

export default withRouter(connect(mapStateToProps, mapDispatchToProps)(SignInContainer))
// export default withRouter(SignInContainer)