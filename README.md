# SyndProxy validated proxy pool

## Current pool

- Alive now: 499
- Gold now: 403
- HTTP: 98 alive / 61 gold
- HTTPS: 42 alive / 17 gold
- SOCKS4: 175 alive / 159 gold
- SOCKS5: 184 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38981
- Ever gold: 1295

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
