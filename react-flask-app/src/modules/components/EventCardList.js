import {
    Button, Card,
    CardActions,
    CardContent,
    CardHeader,
    Divider,
    IconButton,
    List,
    ListItem,
    ListItemAvatar,
    ListItemText
} from "@material-ui/core";
import FolderIcon from "@material-ui/icons/Folder";
import MoreVertIcon from "@material-ui/icons/MoreVert";
import ArrowRightIcon from "@material-ui/icons/ArrowRight";
import React from "react";
import { withStyles } from '@material-ui/core/styles';
import moment from 'moment';

const styles = theme => ({
    nested: {
        paddingLeft: theme.spacing(4),
      },
    content: {
        padding: 0
    },
    image: {
        height: 48,
        width: 48
    },
    actions: {
        justifyContent: 'flex-end'
    }
});

function EventCardList({ title, data, maxItems, avatar, iconButton, chatButton, className, classes }) {
    function setItems(items) {
        if (items.length > maxItems) {
            return data.slice(0, maxItems)
        } else {
            return data
        }
    }

    const points = setItems(data);

    return (
        <Card className={className}>
          <CardHeader
            subtitle={`${points.length} in total`}
            title={title}
          />
          <Divider />
          <CardContent className={classes.content}>
            <List>
              {points
                  .sort((a, b) => moment(a.timeStart) - moment(b.timeStart))
                  .map((point, i) => (
                  <div>
                <ListItem
                  key={i}
                >
                  <ListItemAvatar>
                      {avatar(point.org, point.avatar)}
                    {/*<img*/}
                    {/*  alt="Conversation"*/}
                    {/*  className={classes.image}*/}
                    {/*  src={product.imageUrl}*/}
                    {/*/>*/}
                  </ListItemAvatar>
                  <ListItemText
                    primary={point.displayName}
                    secondary={`${moment(point.timeStart).format('LT')} - ${moment(point.timeEnd).format('h:mm A, MMMM Do YYYY')}`}
                  />
                  {moment().isBefore(moment(point.timeDeadline)) ? iconButton(point.id) : null}
                </ListItem>
                  {point.hasOwnProperty('convos') ?
                          <div>
                              <Divider variant="inset"/>
                              <List component="div" disablePadding>
                                  {point.convos
                                      .sort((a, b) => moment(a.timeStart) - moment(b.timeStart))
                                      .map((convo, i) => (
                                      <ListItem className={classes.nested} key={i}>
                                        <ListItemText
                                          primary={convo.displayName}
                                          secondary={`Start Time: ${moment(convo.timeStart).format('LT')}`}
                                        />
                                          {chatButton(convo.id)}
                                      </ListItem>
                                  ))}
                              </List>
                          </div> : null}
                      <Divider/>
                  </div>
              ))}
            </List>
          </CardContent>
          {/*<CardActions className={classes.actions}>*/}
          {/*  <Button*/}
          {/*    color="primary"*/}
          {/*    size="small"*/}
          {/*    variant="text"*/}
          {/*  >*/}
          {/*    View all <ArrowRightIcon />*/}
          {/*  </Button>*/}
          {/*</CardActions>*/}
        </Card>
    )
}

export default withStyles(styles)(EventCardList);