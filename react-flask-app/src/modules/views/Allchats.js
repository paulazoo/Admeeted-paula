import React, {useState, useEffect, Component } from "react";
import Icon from '@material-ui/core/Icon';
import MainLayout from "../layouts/MainLayout";
import {
    Grid,
    Card,
    CardHeader,
    CardContent,
    CardActions,
    Button,
    TextField,
    Divider,
    List,
    ListItem,
    ListItemAvatar,
    ListItemText,
    IconButton
} from '@material-ui/core';
import ChatIcon from '@material-ui/icons/Chat';
import CardList from "../components/CardList";
import {NavLink} from "react-router-dom";
import { withStyles } from '@material-ui/core/styles';
import ReactJson from "react-json-view";
import Loading from "./Loading";
import io from "socket.io-client";

const styles = theme => ({
    grid: {
        flexGrow: 1,
        padding: theme.spacing(4),
        height: '50%'
    },
    convoRoot: {
        height: '100%'
    },
    image: {
        height: 48
    },
});


function Allchats ({ conversations, currentlySending, classes }) {
    const [values, setValues] = useState({
        error: false
    });

    //console.log(values);

    const handleSubmit = event => {

    };

    const handleChange = event => {
        setValues({
            ...values,
            [event.target.name]: event.target.value,
            error: false
        })
    };

    const handleNumChange = event => {
        setValues({
            ...values,
            [event.target.name]: Number(event.target.value),
            error: false
        })
    };

    //console.log(values);

    const convoText = 'Other Conversations';

    const convoSubtext = 'Revisit the calls you have participated in from past events.';

    const maxItems = 50;

    function avatar(uid, avatar) {
        return <Button
            color="primary"
            edge="end"
            size="small"
            component={NavLink}
            to={`/organization/${uid}`}
        >
            <img
                className={classes.image}
                src={avatar}
                alt='Organization'
            />
        </Button>
    }
    
    function chatButton(convo_id) {
        return <IconButton
            color="primary"
            edge="end"
            size="small"
            component={NavLink}
            to={`/convochat/${convo_id}`}
        >
            <ChatIcon/>
        </IconButton>
    }

    return (
        <Grid item xs={4}>
        <CardList
            title={convoText}
            subheader={convoSubtext}
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
    )
}


export default withStyles(styles)(Allchats);