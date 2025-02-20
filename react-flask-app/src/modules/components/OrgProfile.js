import React, {useState} from 'react';
import PropTypes from 'prop-types';
import clsx from 'clsx';
import moment from 'moment';
import { makeStyles } from '@material-ui/styles';
import {
  Card,
  CardActions,
  CardContent,
  Avatar,
  Typography,
  Divider,
  Button,
  LinearProgress
} from '@material-ui/core';
import OrgCardList from "./OrgCardList";
import OrgJoinDialog from "./OrgJoinDialog";

const useStyles = makeStyles(theme => ({
  root: {},
  details: {
    display: 'flex'
  },
  avatar: {
    marginLeft: 'auto',
    height: 110,
    width: 100,
    flexShrink: 0,
    flexGrow: 0
  },
  progress: {
    marginTop: theme.spacing(2)
  },
  uploadButton: {
    marginRight: theme.spacing(2)
  }
}));

function OrgProfile ({ user, org_uid, modifyOrgMembership, className, ...rest }) {
  const classes = useStyles();
  const [open, setOpen] = useState(false);

  const handleClickOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };

  function changeOrgMembership() {
    if (!user.joined && user.hasOwnProperty('passcode')) {
      handleClickOpen();
    }
    else {
      modifyOrgMembership(!user.joined, org_uid)
    }
  }

  function joinOrganization() {
    modifyOrgMembership(true, org_uid)
  }

  return (
    <div>
      <Card
        {...rest}
        className={clsx(classes.root, className)}
      >
        <CardContent>
          <div className={classes.details}>
            <div>
              <Typography
                gutterBottom
                variant="h2"
              >
                {user.displayName}
              </Typography>
              <Typography
                className={classes.locationText}
                color="textSecondary"
                variant="body1"
              >
                {user.description}
              </Typography>
              <Typography
                className={classes.dateText}
                color="textSecondary"
                variant="body1"
              >
                {`Founded: ${moment(user.dateFounded).format('MMMM Do YYYY')}`}
              </Typography>
            </div>
            <Avatar
              className={classes.avatar}
              src={user.avatar}
            />
          </div>
          {/*<div className={classes.progress}>*/}
          {/*  <Typography variant="body1">Profile Completeness: 70%</Typography>*/}
          {/*  <LinearProgress*/}
          {/*    value={70}*/}
          {/*    variant="determinate"*/}
          {/*  />*/}
          {/*</div>*/}
        </CardContent>
        <Divider />
        <CardActions>
          <Button
            className={classes.uploadButton}
            color="primary"
            variant="text"
            onClick={changeOrgMembership}
          >
            {user.joined ? 'Leave organization' : 'Join organization'}
          </Button>
          {user.admin ? <Button variant="text">Manage</Button> : null}
        </CardActions>
      </Card>
      <OrgJoinDialog passcode={user.passcode} open={open} handleClose={handleClose} joinOrganization={joinOrganization}/>
    </div>
  );
};

OrgProfile.propTypes = {
  className: PropTypes.string
};

export default OrgProfile;