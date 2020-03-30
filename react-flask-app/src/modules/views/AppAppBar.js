import React, {useState} from 'react';
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
import EventIcon from '@material-ui/icons/Event';
import {IconButton} from "@material-ui/core";
import AccountCircleIcon from '@material-ui/icons/AccountCircle';
import ExitToAppIcon from '@material-ui/icons/ExitToApp';
import SearchIcon from '@material-ui/icons/Search';
import {GoogleLogout} from "react-google-login";
import Button from "../components/Button";
import {logout} from "../actions";
import SearchBarDialogContainer from "../containers/SearchBarDialogContainer";

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

function AppAppBar({ loggedIn, handleLogout, classes }) {
  const [open, setOpen] = useState(false);

  const handleClickOpen = () => {
    console.log(open);
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };

  const logoutGoogle = () => {
    console.log('User log out');
    handleLogout();
  };

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
                <IconButton
                  color="inherit"
                  className={classes.rightLink}
                  onClick={handleClickOpen}
              >
                <SearchIcon/>
              </IconButton>
                    <IconButton
                  color="inherit"
                  className={classes.rightLink}
                  component={NavLink}
                  to="/events"
              >
                <EventIcon/>
              </IconButton>
                  <IconButton
                  color="inherit"
                  className={classes.rightLink}
                  component={NavLink}
                  to="/account"
              >
                <AccountCircleIcon/>
              </IconButton>
                <GoogleLogout
                  clientId="667088492207-2fch6bc6r8b40fm40hjv8mq0n6minrr2.apps.googleusercontent.com"
                  buttonText="Logout"
                  render={renderProps => (
                      <IconButton
                          color="inherit"
                          className={classes.rightLink}
                          onClick={renderProps.onClick}
                          disabled={renderProps.disabled}
                      >
                        <ExitToAppIcon/>
                      </IconButton>
                  )}
                  onLogoutSuccess={logoutGoogle}
              >
              </GoogleLogout>
              </div> : null}
              {/*{!loggedIn ? <Link*/}
              {/*    variant="h6"*/}
              {/*    underline="none"*/}
              {/*    className={clsx(classes.rightLink, classes.linkSecondary)}*/}
              {/*    component={NavLink}*/}
              {/*    to="/sign-up"*/}
              {/*>*/}
              {/*  {'Sign Up'}*/}
              {/*</Link> : null}*/}
            </div>
          </Toolbar>
        </AppBar>
        <div className={classes.placeholder}/>
        <SearchBarDialogContainer open={open} handleClose={handleClose}/>
      </div>
  );
}

AppAppBar.propTypes = {
  classes: PropTypes.object.isRequired,
};

const mapStateToProps = state => ({
  loggedIn: state.loggedIn
})

const mapDispatchToProps = dispatch => ({
    handleLogout: () => dispatch(logout())
})

export default compose(
    withStyles(styles),
    connect(mapStateToProps, mapDispatchToProps)
    )(AppAppBar);
