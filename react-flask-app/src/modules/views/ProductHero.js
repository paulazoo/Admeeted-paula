import React from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import Button from '../components/Button';
import Typography from '../components/Typography';
import ProductHeroLayout from '../layouts/ProductHeroLayout';
import {NavLink, Redirect} from 'react-router-dom';
import {compose} from "redux";
import {connect} from "react-redux";
import {GoogleLogin} from "react-google-login";
import {login} from "../actions";

const backgroundImage =
  'https://www.insidehighered.com/sites/default/server_files/media/image_4.png';

const styles = theme => ({
  background: {
    backgroundImage: `url(${backgroundImage})`,
    backgroundColor: '#7fc7d9', // Average color of the background image.
    backgroundPosition: 'center',
  },
  button: {
    minWidth: 200,
  },
  h5: {
    marginBottom: theme.spacing(4),
    marginTop: theme.spacing(4),
    [theme.breakpoints.up('sm')]: {
      marginTop: theme.spacing(10),
    },
  },
  more: {
    marginTop: theme.spacing(2),
  },
});

function ProductHero({ loggedIn, googleLogin, classes }) {
  const successGoogle = (response) => {
    console.log(response);
    googleLogin(response['profileObj'])
  }

  const failureGoogle = (response) => {
    console.log(response);
  }


  return (
      <div>
        {loggedIn ? (
            <Redirect to='/home' />
            ) : (
            <div>
              <ProductHeroLayout backgroundClassName={classes.background}>
                {/* Increase the network loading priority of the background image. */}
                <img style={{ display: 'none' }} src={backgroundImage} alt="increase priority" />
                <Typography color="inherit" align="center" variant="h2" marked="center">
                  Discover New Friends
                </Typography>
                 <Typography color="inherit" align="center" variant="h5" className={classes.h5}>
                  They're waiting for you.
                </Typography>
                <Typography color="inherit" align="center" variant="h5" className={classes.h5}>
                  Meet your fellow Harvard admitted students - new connections, just one click away.
                </Typography>
                <GoogleLogin
                  clientId="667088492207-2fch6bc6r8b40fm40hjv8mq0n6minrr2.apps.googleusercontent.com"
                  buttonText="Login"
                  render={renderProps => (
                      <Button
                        color="secondary"
                        variant="contained"
                        size="large"
                        className={classes.button}
                        onClick={renderProps.onClick}
                        disabled={renderProps.disabled}
                      >
                        Sign In With Google
                      </Button>
                  )}
                  onSuccess={successGoogle}
                  onFailure={failureGoogle}
                  cookiePolicy={'single_host_origin'}
                />

                <Typography variant="body2" color="inherit" className={classes.more}>
                  Take a chance!
                </Typography>
              </ProductHeroLayout>
            </div>
        )}
      </div>
  );
}

ProductHero.propTypes = {
  classes: PropTypes.object.isRequired,
};

const mapStateToProps = state => ({
  loggedIn: state.loggedIn
})

const mapDispatchToProps = dispatch => ({
    googleLogin: (profile) => {
        dispatch(login(profile))
    }
})

export default compose(
    withStyles(styles),
    connect(mapStateToProps, mapDispatchToProps)
    )(ProductHero);
