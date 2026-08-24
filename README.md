# SyndProxy validated proxy pool

## Current pool

- Alive now: 503
- Gold now: 389
- HTTP: 107 alive / 60 gold
- HTTPS: 53 alive / 13 gold
- SOCKS4: 162 alive / 156 gold
- SOCKS5: 181 alive / 160 gold

## Historical pool

- Discovered: 175458
- Ever alive: 33193
- Ever gold: 1230

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
