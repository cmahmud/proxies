# SyndProxy validated proxy pool

## Current pool

- Alive now: 558
- Gold now: 419
- HTTP: 95 alive / 74 gold
- HTTPS: 102 alive / 20 gold
- SOCKS4: 177 alive / 159 gold
- SOCKS5: 184 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42514
- Ever gold: 1358

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
