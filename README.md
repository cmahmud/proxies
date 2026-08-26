# SyndProxy validated proxy pool

## Current pool

- Alive now: 576
- Gold now: 404
- HTTP: 110 alive / 60 gold
- HTTPS: 88 alive / 13 gold
- SOCKS4: 177 alive / 159 gold
- SOCKS5: 201 alive / 172 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38211
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
