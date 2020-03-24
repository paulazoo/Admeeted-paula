import React from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import Button from '../components/Button';
import Typography from '../components/Typography';
import ProductHeroLayout from './ProductHeroLayout';
import {NavLink, Redirect} from 'react-router-dom';

const backgroundImage =
  'https://assets.rbl.ms/11259921/origin.jpg';

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

function ProductHero(props) {
  const { classes } = props;
  const isLoggedIn = false;

  return (
      <div>
        {isLoggedIn ? (
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
                  Meet the people you vibe with through our data-driven video-conferencing platform.
                </Typography>
                <Button
                  color="secondary"
                  variant="contained"
                  size="large"
                  className={classes.button}
                  component={NavLink}
                  to="/sign-up"
                >
                  Register
                </Button>
                <Typography variant="body2" color="inherit" className={classes.more}>
                  Take a chance
                </Typography>
              </ProductHeroLayout>
              <iframe
                  src="https://docs.google.com/forms/d/e/1FAIpQLScrrI4c-SRt6blejIZLADnBDt98UUg-2pMxrfMiChnDykhkGw/viewform?embedded=true"
                  width="640" height="2513" frameBorder="0" marginHeight="0" marginWidth="0">Loading…
              </iframe>
            </div>
        )}
      </div>
  );
}

ProductHero.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(ProductHero);
