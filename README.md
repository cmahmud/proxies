# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 388
- HTTP: 106 alive / 60 gold
- HTTPS: 53 alive / 12 gold
- SOCKS4: 161 alive / 156 gold
- SOCKS5: 182 alive / 160 gold

## Historical pool

- Discovered: 175458
- Ever alive: 33193
- Ever gold: 1230

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
