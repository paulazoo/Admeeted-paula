import React from 'react';
import { withStyles } from '@material-ui/core/styles';
import {Grid, IconButton} from "@material-ui/core";
import CardList from "./CardList";
import OrgCardList from "./OrgCardList";
import {NavLink} from "react-router-dom";
import FolderIcon from "@material-ui/icons/Folder";
import ChatIcon from "@material-ui/icons/Chat";
import ArrowRightIcon from "@material-ui/icons/ArrowRight";
import AddIcon from "@material-ui/icons/Add";
import RemoveIcon from "@material-ui/icons/Remove";

const styles = theme => ({
    grid: {
        flexGrow: 1,
        padding: theme.spacing(4),
    },
    upcomingRoot: {
        height: '100%'
    },
    availRoot: {
        height: '100%'
    },
    convoRoot: {
        height: '100%'
    }
});

function OrgDashboard ({ org_uid, upcomingEvents, availEvents, conversations, modifyEvent, classes }) {
    const maxItems = 5;

    const upcomingText = 'Your upcoming events';
    const convoText = 'Your conversations';
    const availText = 'Your available events';

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

    function addButton(event_uid) {
        function addEvent() {
            modifyEvent(event_uid, true, org_uid)
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
            modifyEvent(event_uid, false, org_uid)
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

    return (
        <Grid
            container
            spacing={4}
            className={classes.grid}
        >
            <Grid
                item
                lg={4}
                md={6}
                xl={4}
                xs={12}
            >
                <OrgCardList
                    title={upcomingText}
                    data={upcomingEvents}
                    maxItems={maxItems}
                    iconButton={removeButton}
                    className={classes.upcomingRoot}
                />
            </Grid>
            <Grid
                item
                lg={4}
                md={6}
                xl={4}
                xs={12}
            >
                <OrgCardList
                    title={availText}
                    data={availEvents}
                    maxItems={maxItems}
                    iconButton={addButton}
                    className={classes.availRoot}
                />
            </Grid>
            <Grid
                item
                lg={4}
                md={6}
                xl={4}
                xs={12}
            >
                <OrgCardList
                    title={convoText}
                    data={conversations}
                    maxItems={maxItems}
                    iconButton={chatButton}
                    className={classes.convoRoot}
                />
            </Grid>
        </Grid>
    )
}

export default withStyles(styles)(OrgDashboard);