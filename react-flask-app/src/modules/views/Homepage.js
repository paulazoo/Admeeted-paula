import React from 'react';
import PropTypes from 'prop-types';
import clsx from 'clsx';
import { withStyles } from '@material-ui/core/styles';
import Typography from '../components/Typography';
import MainLayout from "../layouts/MainLayout";
import {
    Grid,
    Card,
    CardHeader,
    CardContent,
    CardActions,
    Button,
    Divider,
    List,
    ListItem,
    ListItemAvatar,
    ListItemText,
    IconButton
} from '@material-ui/core';
import ArrowRightIcon from '@material-ui/icons/ArrowRight';
import MoreVertIcon from '@material-ui/icons/MoreVert';

import Paper from '../components/Paper';
import Container from '@material-ui/core/Container';
import FolderIcon from '@material-ui/icons/Folder';
import PanelLayout from './PanelLayout';
import Panel from "./Panel";
import PanelList from "./PanelList";
import Loading from "./Loading";
import CardList from "../components/CardList";

const styles = theme => ({
    grid: {
        flexGrow: 1,
        padding: theme.spacing(4),
    },
    upcomingRoot: {
        height: '100%'
    },
    orgsRoot: {
        height: '100%'
    },
    pastRoot: {
        height: '100%'
    }
});

function Homepage({ data, currentlySending, classes }) {
    const upcomingText = 'Your upcoming conversations';
    const pastText = 'Your past conversations';
    const orgText = 'Your organizations';

    const upcomingConvos = data.upcomingConvos;
    const pastConvos = data.pastConvos;
    const organizations = data.organizations;

    const maxItems = 5;

    return(
        <div>
            {!currentlySending ?
            <MainLayout>
                <Grid container className={classes.grid} spacing={4}>
                    <Grid item
                          lg={4}
                          sm={6}
                          xl={4}
                          xs={12}
                    >
                        <CardList title={upcomingText} data={upcomingConvos} maxItems={maxItems} className={classes.upcomingRoot}/>
                        {/*<PanelLayout>*/}
                        {/*    <Panel title={upcomingText}>*/}
                        {/*        <PanelList data={upcomingConvos}/>*/}
                        {/*    </Panel>*/}
                        {/*</PanelLayout>*/}
                    </Grid>
                    <Grid item
                          lg={4}
                          sm={6}
                          xl={4}
                          xs={12}
                    >
                        <CardList title={orgText} data={organizations} maxItems={maxItems} className={classes.orgsRoot}/>
                        {/*<PanelLayout>*/}
                        {/*    <Panel title={orgText}>*/}
                        {/*        <PanelList data={organizations}/>*/}
                        {/*    </Panel>*/}
                        {/*    <Panel title={pastText}>*/}
                        {/*        <PanelList data={pastConvos}/>*/}
                        {/*    </Panel>*/}
                        {/*</PanelLayout>*/}
                    </Grid>
                    <Grid item
                          lg={4}
                          sm={6}
                          xl={4}
                          xs={12}
                    >
                        <CardList title={pastText} data={pastConvos} maxItems={maxItems} className={classes.pastRoot}/>
                        {/*<PanelLayout>*/}
                        {/*    <Panel title={orgText}>*/}
                        {/*        <PanelList data={organizations}/>*/}
                        {/*    </Panel>*/}
                        {/*    <Panel title={pastText}>*/}
                        {/*        <PanelList data={pastConvos}/>*/}
                        {/*    </Panel>*/}
                        {/*</PanelLayout>*/}
                    </Grid>
                </Grid>
            </MainLayout> : <Loading/>}
        </div>
    );
}

Homepage.propTypes = {
    classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(Homepage);