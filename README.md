# SyndProxy validated proxy pool

## Current pool

- Alive now: 482
- Gold now: 399
- HTTP: 98 alive / 60 gold
- HTTPS: 40 alive / 15 gold
- SOCKS4: 167 alive / 159 gold
- SOCKS5: 177 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38970
- Ever gold: 1295

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
