import React, { useEffect, Component } from 'react';
import Homepage from '../views/Homepage';
import { loadData, loadConvochatData } from "../actions";
import { connect } from 'react-redux';
import { withRouter } from 'react-router-dom';
import {Grid, IconButton, Button} from "@material-ui/core";
import MainLayout from "../layouts/MainLayout";
import Convochat from "../views/Convochat";
import Wrongchat from "../views/Wrongchat";
import Allchats from "../views/Allchats";
import Loading from "../views/Loading";
import io from "socket.io-client";

function ConvochatContainer ({
  match,
  data,
  currentlySending,
  loadPastConvos,
  loadConvochat
}) {

  const convo_uid=match.params.convo_uid;

  useEffect(() => {
    loadPastConvos();
    loadConvochat(convo_uid);
  }, [convo_uid]);

  const conversations=data.conversations;
  const userInConvo=data.userInConvo;
  const convoDisplayName=data.convoDisplayName;
  const videolink=data.videolink;
  console.log(videolink)

  return (
    <div>
      {!currentlySending ? <MainLayout>
        <Grid 
        container
        direction="row"
        spacing={2}>
          <Allchats conversations={conversations} currentlySending={currentlySending}/>
          {userInConvo ? <Convochat
          convo_uid={convo_uid} 
          convoDisplayName={convoDisplayName}
          currentlySending={currentlySending}/> : null}
        </Grid>
      </MainLayout> : <Loading/>}
    </div>
  )
}

const mapStateToProps = state => ({
  data: state.data,
  currentlySending: state.currentlySending
})

const mapDispatchToProps = dispatch => ({
  loadPastConvos: () => {
      dispatch(loadData('/past-conversations', 'conversations'));
  },
  loadConvochat: (convo_uid) => {
    dispatch(loadConvochatData(`/convochat/${convo_uid}`, 'userInConvo', 'convoDisplayName', 'videolink'));
  }
})

export default withRouter(connect(mapStateToProps, mapDispatchToProps)(ConvochatContainer))