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

const styles = theme => ({
    flex: {
        display: 'flex',
        flexDirection: 'row',
    },
    content: {
        padding: 0
    },
    image: {
        height: '100%',
        width: 36
    },
    actions: {
        justifyContent: 'flex-end'
    }
});

function OrgsCardList({ title, subheader, data, maxItems, iconButton, className, classes }) {
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
            subheader={subheader}
            title={title}
          />
          <Divider />
          <CardContent className={classes.content}>
            <List
                // className={classes.flex}
            >
              {points.map((point, i) => (
                <ListItem
                  divider={i < points.length}
                  key={i}
                >
                  <ListItemText
                    primary={point.displayName}
                    secondary={"Click to see organization"}
                  />
                    {point.hasOwnProperty('link') ? iconButton(point.link) : iconButton(point.id)}
                </ListItem>
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

// NOT BEING USED RIGHT NOW
export default withStyles(styles)(OrgsCardList);