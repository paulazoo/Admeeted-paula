import React from "react";
import { withStyles } from '@material-ui/core/styles';
import {Grid, IconButton} from '@material-ui/core';
import MainLayout from "../layouts/MainLayout";
import Loading from './Loading';
import OrgProfile from "../components/OrgProfile";
import OrgDashboard from "../components/OrgDashboard";
import Container from "@material-ui/core/Container";
import CardList from "../components/CardList";
import {NavLink} from "react-router-dom";
import FolderIcon from "@material-ui/icons/Folder";
import ChatIcon from "@material-ui/icons/Chat";
import ArrowRightIcon from "@material-ui/icons/ArrowRight";
import OrgDashboardContainer from "../containers/OrgDashboardContainer";

const styles = theme => ({
    root: {
        width: '50vw'
    }
});

function Organization ({ org_data, org_uid, currentlySending, modifyEvent, modifyOrgMembership, classes }) {
    const profile = org_data.profile;
    const upcomingEvents = org_data.upcomingEvents;
    const availEvents = org_data.availEvents;
    const conversations = org_data.conversations;

    console.log(profile.joined)

    return (
        <div>
            {!currentlySending ? <MainLayout>
                <Grid
                    className={classes.root}
                    container
                    spacing={4}
                >
                    <Grid
                        item
                        md={12}
                    >
                        <OrgProfile user={profile} org_uid={org_uid} modifyOrgMembership={modifyOrgMembership} />
                    </Grid>
                </Grid>
                {profile.joined ? <OrgDashboard
                    availEvents={availEvents}
                    upcomingEvents={upcomingEvents}
                    conversations={conversations}
                    modifyEvent={modifyEvent}
                    org_uid={org_uid}/> : null}
            </MainLayout> : <Loading/>}
        </div>
    )
}

export default withStyles(styles)(Organization);