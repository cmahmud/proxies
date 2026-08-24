# SyndProxy validated proxy pool

## Current pool

- Alive now: 494
- Gold now: 389
- HTTP: 102 alive / 61 gold
- HTTPS: 52 alive / 12 gold
- SOCKS4: 159 alive / 156 gold
- SOCKS5: 181 alive / 160 gold

## Historical pool

- Discovered: 175458
- Ever alive: 33193
- Ever gold: 1230

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
