import React from 'react';
import PropTypes from 'prop-types';
import clsx from 'clsx';
import { withStyles } from '@material-ui/core/styles';
import Link from '@material-ui/core/Link';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  NavLink
} from "react-router-dom";
import AppBar from '../components/AppBar';
import SignIn from './SignIn';
import SignUp from './SignUp';
import App from '../../App';
import Toolbar, { styles as toolbarStyles } from '../components/Toolbar';
import { compose } from 'redux';
import { connect } from 'react-redux';

const styles = theme => ({
  title: {
    fontSize: 24,
  },
  placeholder: toolbarStyles(theme).root,
  toolbar: {
    justifyContent: 'space-between',
  },
  left: {
    flex: 1,
  },
  leftLinkActive: {
    color: theme.palette.common.white,
  },
  right: {
    flex: 1,
    display: 'flex',
    justifyContent: 'flex-end',
  },
  rightLink: {
    fontSize: 16,
    color: theme.palette.common.white,
    marginLeft: theme.spacing(3),
  },
  linkSecondary: {
    color: theme.palette.secondary.main,
  },
});

function AppAppBar({ loggedIn, classes }) {

  return (
      <div>
        <AppBar position="fixed">
          <Toolbar className={classes.toolbar}>
            <div className={classes.left}/>
            <Link
                variant="h6"
                underline="none"
                color="inherit"
                className={classes.title}
                component={NavLink}
                to="/"
            >
              {'Admeeted'}
            </Link>
            <div className={classes.right}>
              {loggedIn ? <div>
                    <Link
                  color="inherit"
                  variant="h6"
                  underline="none"
                  className={classes.rightLink}
                  component={NavLink}
                  to="/conversations"
              >
                Convos
              </Link>
                  <Link
                  color="inherit"
                  variant="h6"
                  underline="none"
                  className={classes.rightLink}
                  component={NavLink}
                  to="/account"
              >
                Acct
              </Link>
              </div>: null}
              {!loggedIn ? <Link
                  color="inherit"
                  variant="h6"
                  underline="none"
                  className={classes.rightLink}
                  component={NavLink}
                  to="/sign-in"
              >
                Sign In
              </Link> : <Link
                  color="inherit"
                  variant="h6"
                  underline="none"
                  className={classes.rightLink}
                  component={NavLink}
                  to="/sign-out"
              >
                Sign Out
              </Link>}
              {!loggedIn ? <Link
                  variant="h6"
                  underline="none"
                  className={clsx(classes.rightLink, classes.linkSecondary)}
                  component={NavLink}
                  to="/sign-up"
              >
                {'Sign Up'}
              </Link> : null}
            </div>
          </Toolbar>
        </AppBar>
        <div className={classes.placeholder}/>
      </div>
  );
}

AppAppBar.propTypes = {
  classes: PropTypes.object.isRequired,
};

const mapStateToProps = state => ({
  loggedIn: state.loggedIn
})

export default compose(
    withStyles(styles),
    connect(mapStateToProps, null)
    )(AppAppBar);
