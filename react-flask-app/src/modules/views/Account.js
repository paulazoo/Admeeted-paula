import React from 'react';
import { Grid } from '@material-ui/core';

import AccountProfile from '../components/AccountProfile';
import AccountDetails from '../components/AccountDetails';
import MainLayout from "../layouts/MainLayout";
import Loading from './Loading';
import {withStyles} from "@material-ui/core/styles";
import FolderIcon from "@material-ui/icons/Folder";

const styles = theme => ({
  root: { },
});

function Account({ profile, currentlySending, setProfile, classes }) {
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
            <AccountDetails profile={profile} setProfile={setProfile}/>
          </Grid>
       </Grid>
      </MainLayout> : <Loading/>}

    </div>
  );
};

export default withStyles(styles)(Account);