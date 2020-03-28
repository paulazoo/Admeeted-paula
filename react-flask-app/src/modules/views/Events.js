import React from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import Typography from '../components/Typography';
import MainLayout from "../layouts/MainLayout";
import Grid from '@material-ui/core/Grid';
import Paper from '../components/Paper';
import Container from '@material-ui/core/Container';
import PanelLayout from './PanelLayout';
import Panel from "./Panel";
import PanelList from "./PanelList";
import Loading from "./Loading";
import EventCardList from '../components/EventCardList';
import FolderIcon from "@material-ui/icons/Folder";
import {IconButton} from "@material-ui/core";
import MoreVertIcon from "@material-ui/icons/MoreVert";
import AddIcon from "@material-ui/icons/Add";
import RemoveIcon from "@material-ui/icons/Remove";
import {NavLink} from "react-router-dom";

const styles = theme => ({
    root: {
        flexGrow: 1,
    },
    upcomingRoot: {
        height: '100%'
    },
    availRoot: {
        height: '100%'
    }
});

function Events({ data, currentlySending, modifyEvent, classes }) {
    const upcomingText = 'Your upcoming events';
    const availText = 'Your available events';

    const upcomingEvents = data.upcomingEvents;
    const availEvents = data.availEvents;

    const maxItems = 10;

    function avatar(org_uid) {
        return <IconButton
            color="primary"
            edge="end"
            size="small"
            component={NavLink}
            to={`/organization/${org_uid}`}
        >
            <FolderIcon/>
        </IconButton>
    }

    function addButton(event_uid) {
        function addEvent() {
            modifyEvent(event_uid, true)
        }
        return <IconButton
            color="primary"
            edge="end"
            size="small"
            onClick={addEvent}
        >
            <AddIcon/>
        </IconButton>
    }

    function removeButton(event_uid) {
        function removeEvent() {
            modifyEvent(event_uid, false)
        }
        return <IconButton
            color="primary"
            edge="end"
            size="small"
            onClick={removeEvent}
        >
            <RemoveIcon />
        </IconButton>
    }

    return(
        <div>
            {!currentlySending ? <MainLayout>
            <Grid container className={classes.root} spacing={4}>
                <Grid item
                    lg={6}
                    sm={6}
                    xl={6}
                    xs={12}
                >
                    <EventCardList
                        title={upcomingText}
                        data={upcomingEvents}
                        maxItems={maxItems}
                        avatar={avatar}
                        iconButton={removeButton}
                        className={classes.upcomingRoot}
                    />
                    {/*<PanelLayout>*/}
                    {/*    <Panel title={upcomingText}>*/}
                    {/*        <PanelList data={upcomingConvos}/>*/}
                    {/*    </Panel>*/}
                    {/*</PanelLayout>*/}
                </Grid>
                <Grid item
                    lg={6}
                    sm={6}
                    xl={6}
                    xs={12}
                >
                    <EventCardList
                        title={availText}
                        data={availEvents}
                        maxItems={maxItems}
                        avatar={avatar}
                        iconButton={addButton}
                        className={classes.availRoot}
                    />
                    {/*<PanelLayout>*/}
                    {/*    <Panel title={availText}>*/}
                    {/*        <PanelList data={availConvos}/>*/}
                    {/*    </Panel>*/}
                    {/*</PanelLayout>*/}
                </Grid>
            </Grid>
        </MainLayout> : <Loading/>}
        </div>
    );
}

Events.propTypes = {
    classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(Events);