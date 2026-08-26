# SyndProxy validated proxy pool

## Current pool

- Alive now: 492
- Gold now: 401
- HTTP: 96 alive / 60 gold
- HTTPS: 41 alive / 15 gold
- SOCKS4: 165 alive / 161 gold
- SOCKS5: 190 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38979
- Ever gold: 1295

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
