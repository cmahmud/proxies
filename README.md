# SyndProxy validated proxy pool

## Current pool

- Alive now: 504
- Gold now: 403
- HTTP: 89 alive / 65 gold
- HTTPS: 71 alive / 19 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 172 alive / 159 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37727
- Ever gold: 1287

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
