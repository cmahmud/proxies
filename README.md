# SyndProxy validated proxy pool

## Current pool

- Alive now: 509
- Gold now: 415
- HTTP: 95 alive / 66 gold
- HTTPS: 67 alive / 22 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 178 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37047
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
