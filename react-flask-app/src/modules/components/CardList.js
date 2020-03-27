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

function CardList({ title, data, maxItems, className, classes }) {
    var points;
    if (data.length > maxItems) {
        points = data.slice(0, maxItems)
    } else {
        points = data
    }

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
                  divider={i < points.length - 1}
                  key={i}
                >
                  <ListItemAvatar>
                      <FolderIcon/>
                    {/*<img*/}
                    {/*  alt="Conversation"*/}
                    {/*  className={classes.image}*/}
                    {/*  src={product.imageUrl}*/}
                    {/*/>*/}
                  </ListItemAvatar>
                  <ListItemText
                    primary={point.displayName}
                    secondary={point.time}
                  />
                  <IconButton
                    edge="end"
                    size="small"
                  >
                    <MoreVertIcon />
                  </IconButton>
                </ListItem>
              ))}
            </List>
          </CardContent>
          <Divider />
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

export default withStyles(styles)(CardList);