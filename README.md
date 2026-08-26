# SyndProxy validated proxy pool

## Current pool

- Alive now: 500
- Gold now: 404
- HTTP: 85 alive / 60 gold
- HTTPS: 62 alive / 17 gold
- SOCKS4: 166 alive / 161 gold
- SOCKS5: 187 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38547
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
