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

function OrgCardList({ title, data, maxItems, iconButton, className, classes }) {
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
              {points.map((point, i) => (
                <ListItem
                  divider={i < points.length}
                  key={i}
                >
                  <ListItemText
                    primary={point.displayName}
                    secondary={point.timeStart}
                  />
                    {point.hasOwnProperty('link') ? iconButton(point.link) : iconButton(point.id)}
                </ListItem>
              ))}
            </List>
          </CardContent>
          <CardActions className={classes.actions}>
            <Button
              color="primary"
              size="small"
              variant="text"
            >
              View all <ArrowRightIcon />
            </Button>
          </CardActions>
        </Card>
    )
}

export default withStyles(styles)(OrgCardList);