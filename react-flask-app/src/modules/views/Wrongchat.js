import React, {useState, useEffect, Component } from "react";
import Icon from '@material-ui/core/Icon';
import MainLayout from "../layouts/MainLayout";
import {
    Select,
    TextField,
    MenuItem,
    Card,
    CardHeader,
    CardContent,
    CardActions,
    Divider,
    InputLabel,
    FormControl,
    Typography,
    Button,
    IconButton,
    Grid
} from "@material-ui/core";
import { withStyles } from '@material-ui/core/styles';
import ReactJson from "react-json-view";
import Loading from "./Loading";

const styles = theme => ({
    root: {
        width: 500
    },
    json: {
        overflow: 'auto'
    },
    grid: {
        flexGrow: 1,
        padding: theme.spacing(4),
        height: '50%'
    }
});

function Wrongchat ({ events, currentlySending, classes }) {

    return (
    <Grid item xs={8}>
        <Card>
            <CardHeader title={""}/>
            <Divider/>
            <CardContent>
                <Grid
                container
                direction="column">
                    <Grid item xs>
                        <h1>Hmmm... wrong chat?</h1>
                    </Grid>
                </Grid>
            </CardContent>
            <CardActions>

            </CardActions>
        </Card>
    </Grid>
    )
  }


export default withStyles(styles)(Wrongchat);