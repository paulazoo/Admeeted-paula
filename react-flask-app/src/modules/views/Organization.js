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

});

function Organization ({ org_data, org_uid, currentlySending, modifyEvent, classes }) {
    const profile = org_data.profile;
    const upcomingEvents = org_data.upcomingEvents;
    const availEvents = org_data.availEvents;
    const conversations = org_data.conversations;

    return (
        <div>
            {!currentlySending ? <MainLayout>
                <Grid
                    container
                    spacing={4}
                    alignItems="center"
                    justify="center"
                >
                    <Grid
                        item
                        lg={6}
                        md={8}
                        xl={6}
                        xs={12}
                    >
                        <OrgProfile user={profile} />
                    </Grid>
                </Grid>
                <OrgDashboard
                    availEvents={availEvents}
                    upcomingEvents={upcomingEvents}
                    conversations={conversations}
                    modifyEvent={modifyEvent}
                    org_uid={org_uid}/>
            </MainLayout> : <Loading/>}
        </div>
    )
}

export default withStyles(styles)(Organization);