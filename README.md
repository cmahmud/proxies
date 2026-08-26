# SyndProxy validated proxy pool

## Current pool

- Alive now: 575
- Gold now: 404
- HTTP: 101 alive / 60 gold
- HTTPS: 86 alive / 14 gold
- SOCKS4: 186 alive / 162 gold
- SOCKS5: 202 alive / 168 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38156
- Ever gold: 1289

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
