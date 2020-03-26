import React from 'react';
import { makeStyles } from '@material-ui/styles';
import { Grid } from '@material-ui/core';

import AccountProfile from '../components/AccountProfile';
import AccountDetails from '../components/AccountDetails';
import MainLayout from "../layouts/MainLayout";
import Loading from './Loading';
import {withStyles} from "@material-ui/core/styles";

const styles = theme => ({
  root: {
    padding: theme.spacing(4),
    backgroundColor: '#7fc7d9',
    position: 'relative',
    display: 'flex',
    [theme.breakpoints.up('sm')]: {
      height: '100vh',
      minHeight: 500
    },
  },
});

function Account({ profile, currentlySending, classes }) {
  console.log(profile);
  return (
    <div>
      {!currentlySending ? <MainLayout>
        <Grid
          container
          spacing={4}
        >
          <Grid
            item
            lg={4}
            md={6}
            xl={4}
            xs={12}
          >
            <AccountProfile user={profile} />
          </Grid>
          <Grid
            item
            lg={8}
            md={6}
            xl={8}
            xs={12}
          >
            <AccountDetails />
          </Grid>
       </Grid>
      </MainLayout> : <Loading/>}

    </div>
  );
};

export default withStyles(styles)(Account);