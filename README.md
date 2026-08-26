# SyndProxy validated proxy pool

## Current pool

- Alive now: 509
- Gold now: 404
- HTTP: 94 alive / 60 gold
- HTTPS: 63 alive / 17 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 185 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38985
- Ever gold: 1295

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
