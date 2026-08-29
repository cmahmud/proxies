# SyndProxy validated proxy pool

## Current pool

- Alive now: 489
- Gold now: 386
- HTTP: 89 alive / 61 gold
- HTTPS: 66 alive / 15 gold
- SOCKS4: 166 alive / 158 gold
- SOCKS5: 168 alive / 152 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43454
- Ever gold: 1371

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
