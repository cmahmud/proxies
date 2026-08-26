# SyndProxy validated proxy pool

## Current pool

- Alive now: 504
- Gold now: 403
- HTTP: 100 alive / 60 gold
- HTTPS: 56 alive / 17 gold
- SOCKS4: 165 alive / 160 gold
- SOCKS5: 183 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38991
- Ever gold: 1295

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
