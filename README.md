# SyndProxy validated proxy pool

## Current pool

- Alive now: 489
- Gold now: 401
- HTTP: 85 alive / 56 gold
- HTTPS: 49 alive / 17 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 180 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41643
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
