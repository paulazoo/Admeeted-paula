import React from 'react';
import PropTypes from 'prop-types';
import clsx from 'clsx';
import { withStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';
import AppAppBar from "../views/AppAppBar";

const styles = theme => ({
  root: {
    color: theme.palette.common.white,
    position: 'relative',
    display: 'flex',
    backgroundColor: theme.palette.secondary.light,
    [theme.breakpoints.up('sm')]: {
      minHeight: '100vh'
    },
  },
  container: {
    marginTop: theme.spacing(3),
    marginBottom: theme.spacing(14),
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
  },
});

function MainLayout(props) {
  const { children, classes } = props;

  return (
      <section className={classes.root}>
      <Container className={classes.container}>
        {children}
      </Container>
    </section>
  );
}

MainLayout.propTypes = {
  children: PropTypes.node.isRequired,
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(MainLayout);
