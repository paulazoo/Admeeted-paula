import React from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import Grid from '@material-ui/core/Grid';
import Container from '@material-ui/core/Container';
import Button from '../components/Button';
import Typography from '../components/Typography';
import {ReactComponent as CalendarSvg} from "../../images/calendar.svg";
import {ReactComponent as NetworkSvg} from "../../images/network.svg";
import {ReactComponent as UserSvg} from "../../images/user.svg";

const styles = theme => ({
  root: {
    display: 'flex',
    backgroundColor: theme.palette.secondary.light,
    overflow: 'hidden',
  },
  container: {
    marginTop: theme.spacing(10),
    marginBottom: theme.spacing(15),
    position: 'relative',
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
  },
  item: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    padding: theme.spacing(0, 5),
  },
  title: {
    marginBottom: theme.spacing(14),
  },
  number: {
    fontSize: 24,
    fontFamily: theme.typography.fontFamily,
    color: theme.palette.secondary.main,
    fontWeight: theme.typography.fontWeightMedium,
  },
  image: {
    height: 55,
    marginTop: theme.spacing(4),
    marginBottom: theme.spacing(4),
  },
  curvyLines: {
    pointerEvents: 'none',
    position: 'absolute',
    top: -180,
    opacity: 0.7,
  },
  button: {
    marginTop: theme.spacing(8),
  },
});

function ProductHowItWorks({ googleButton, classes }) {
  const getStartedLabel = "Get Started"

  return (
      <div>
    <section className={classes.root}>
      <Container className={classes.container}>
        {/*<img*/}
        {/*  src="../../images/productCurvyLines.png"*/}
        {/*  className={classes.curvyLines}*/}
        {/*  alt="curvy lines"*/}
        {/*/>*/}
        <Typography variant="h4" marked="center" className={classes.title} component="h2">
          How it works
        </Typography>
        <div>
          <Grid container spacing={5}>
            <Grid item xs={12} md={4}>
              <div className={classes.item}>
                <div className={classes.number}>1.</div>
                {/*<img*/}
                {/*  src="/images/themes/onepirate/productHowItWorks1.svg"*/}
                {/*  alt="suitcase"*/}
                {/*  className={classes.image}*/}
                {/*/>*/}
                <UserSvg className={classes.image}/>
                <Typography variant="h5" align="center">
                  Create an account and complete your profile.
                </Typography>
              </div>
            </Grid>
            <Grid item xs={12} md={4}>
              <div className={classes.item}>
                <div className={classes.number}>2.</div>
                {/*<img*/}
                {/*  src="/images/themes/onepirate/productHowItWorks2.svg"*/}
                {/*  alt="graph"*/}
                {/*  className={classes.image}*/}
                {/*/>         */}
                <NetworkSvg className={classes.image}/>
                <Typography variant="h5" align="center">
                  Join organizations and sign up for their events to meet other people.
                </Typography>
              </div>
            </Grid>
            <Grid item xs={12} md={4}>
              <div className={classes.item}>
                <div className={classes.number}>3.</div>
                {/*<img*/}
                {/*  src="../../../public/images/video-call.svg"*/}
                {/*  alt="clock"*/}
                {/*  className={classes.image}*/}
                {/*/>*/}
                <CalendarSvg className={classes.image}/>
                <Typography variant="h5" align="center">
                  New events every week - making friends virtually has never been so easy!
                </Typography>
              </div>
            </Grid>
          </Grid>
        </div>
        {googleButton(getStartedLabel, classes.button)}
        {/*<Button*/}
        {/*  color="secondary"*/}
        {/*  size="large"*/}
        {/*  variant="contained"*/}
        {/*  className={classes.button}*/}
        {/*  component="a"*/}
        {/*  href="/premium-themes/onepirate/sign-up/"*/}
        {/*>*/}
        {/*  Get started*/}
        {/*</Button>*/}
      </Container>
    </section>
        <div className={classes.root}>
          Icons made by <a href="https://www.flaticon.com/authors/smashicons" title="Smashicons">Smashicons</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a>
        </div>
      </div>
  );
}

ProductHowItWorks.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(ProductHowItWorks);
