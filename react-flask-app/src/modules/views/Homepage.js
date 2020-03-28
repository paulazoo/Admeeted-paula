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
import ChatIcon from '@material-ui/icons/Chat';

import Paper from '../components/Paper';
import Container from '@material-ui/core/Container';
import FolderIcon from '@material-ui/icons/Folder';
import PanelLayout from './PanelLayout';
import Panel from "./Panel";
import PanelList from "./PanelList";
import Loading from "./Loading";
import CardList from "../components/CardList";
import {NavLink} from "react-router-dom";
import OrgCardList from "../components/OrgCardList";

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
    convoRoot: {
        height: '100%'
    },
    image: {
        height: 36,
        width: 36
    }
});

function Homepage({ data, currentlySending, classes }) {
    const upcomingText = 'Your upcoming events';
    const convoText = 'Your conversations';
    const orgText = 'Your organizations';

    const viewAllConvos = ''; // What is this for?

    const upcomingEvents = data.upcomingEvents;
    const conversations = data.conversations;
    const organizations = data.organizations;

    console.log(data);

    const maxItems = 5;

    function avatar(uid) {
        return <Button
            color="primary"
            edge="end"
            size="small"
            component={NavLink}
            to={`/organization/${uid}`}
        >
            <img
                className={classes.image}
                src='/logo192.png'
                alt='React'
            />
        </Button>
    }

    function chatButton(link) {
        console.log(link);
        return <IconButton
            color="primary"
            edge="end"
            size="small"
            href={link}
        >
            <ChatIcon/>
        </IconButton>
    }

    function arrowButton(uid) {
        return <IconButton
            color="primary"
            edge="end"
            size="small"
            component={NavLink}
            to={`/organization/${uid}`}
        >
            <ArrowRightIcon />
        </IconButton>
    }

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
                        <CardList
                            title={upcomingText}
                            data={upcomingEvents}
                            maxItems={maxItems}
                            avatar={avatar}
                            iconButton={chatButton}
                            className={classes.upcomingRoot}
                        />
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
                        <OrgCardList
                            title={orgText}
                            data={organizations}
                            maxItems={maxItems}
                            avatar={avatar}
                            iconButton={arrowButton}
                            className={classes.orgsRoot}
                        />
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
                        <CardList
                            title={convoText}
                            data={conversations}
                            maxItems={maxItems}
                            avatar={avatar}
                            iconButton={chatButton}
                            className={classes.convoRoot}
                        />
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