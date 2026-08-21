# SyndProxy private pool

## Current pool

- Alive now: 1102
- Gold now: 384
- HTTP: 363 alive / 102 gold
- HTTPS: 274 alive / 26 gold
- SOCKS4: 207 alive / 121 gold
- SOCKS5: 258 alive / 135 gold

## Historical pool

- Discovered: 152221
- Ever alive: 27972
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
