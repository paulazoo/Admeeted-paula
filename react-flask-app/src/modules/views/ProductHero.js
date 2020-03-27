import React from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import Button from '../components/Button';
import Typography from '../components/Typography';
import ProductHeroLayout from '../layouts/ProductHeroLayout';
import {NavLink, Redirect} from 'react-router-dom';
import {compose} from "redux";
import {connect} from "react-redux";

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

function ProductHero({ loggedIn, classes }) {

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
                  Meet your fellow Harvard admitted students - new connections, just one click away.
                </Typography>
                <Button
                  color="secondary"
                  variant="contained"
                  size="large"
                  className={classes.button}
                  component={NavLink}
                  to="/sign-up"
                >
                  Sign Up
                </Button>
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

export default compose(
    withStyles(styles),
    connect(mapStateToProps, null)
    )(ProductHero);
