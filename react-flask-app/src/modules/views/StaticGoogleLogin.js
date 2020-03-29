import React from 'react';
import { GoogleLogin, GoogleLogout } from "react-google-login";
import { connect } from 'react-redux';
import { login } from "../actions";

function StaticGoogleLogin({ googleLogin }) {
    const responseGoogle = (response) => {
      console.log(response);
      googleLogin(response['profileObj'])
    }

    const logout = (response) => {
        console.log(response)
    }

    return (
        <div>
            <GoogleLogin
                clientId="667088492207-2fch6bc6r8b40fm40hjv8mq0n6minrr2.apps.googleusercontent.com"
                buttonText="Login"
                render={renderProps => (
                  <button onClick={renderProps.onClick} disabled={renderProps.disabled}>This is my custom Google button</button>
                )}
                onSuccess={responseGoogle}
                onFailure={responseGoogle}
                cookiePolicy={'single_host_origin'}
              />
            <GoogleLogout
                clientId="667088492207-2fch6bc6r8b40fm40hjv8mq0n6minrr2.apps.googleusercontent.com"
                buttonText="Logout"
                onLogoutSuccess={logout}
            >
            </GoogleLogout>
        </div>

    )
}

const mapDispatchToProps = dispatch => ({
    googleLogin: (profile) => {
        dispatch(login(profile))
    }
})

export default connect(null, mapDispatchToProps)(StaticGoogleLogin);