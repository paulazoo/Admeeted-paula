import React from 'react';
import { withStyles } from '@material-ui/core/styles';
import CircularProgress from '@material-ui/core/CircularProgress';
import MainLayout from "../layouts/MainLayout";

const styles = theme => ({
  root: {
    width: '100%',
  },
})

function Loading () {
  return <MainLayout> <CircularProgress color="secondary" /> </MainLayout>
}

export default withStyles(styles)(Loading);