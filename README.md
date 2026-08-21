# SyndProxy private pool

## Current pool

- Alive now: 1093
- Gold now: 383
- HTTP: 364 alive / 99 gold
- HTTPS: 274 alive / 28 gold
- SOCKS4: 203 alive / 121 gold
- SOCKS5: 252 alive / 135 gold

## Historical pool

- Discovered: 152221
- Ever alive: 27980
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
