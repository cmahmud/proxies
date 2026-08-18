# SyndProxy private pool

## Current pool

- Alive now: 678
- Gold now: 213
- HTTP: 189 alive / 27 gold
- HTTPS: 99 alive / 8 gold
- SOCKS4: 206 alive / 102 gold
- SOCKS5: 184 alive / 76 gold

## Historical pool

- Discovered: 86694
- Ever alive: 6452
- Ever gold: 296

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
