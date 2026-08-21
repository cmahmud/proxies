# SyndProxy private pool

## Current pool

- Alive now: 1160
- Gold now: 389
- HTTP: 411 alive / 102 gold
- HTTPS: 276 alive / 30 gold
- SOCKS4: 211 alive / 121 gold
- SOCKS5: 262 alive / 136 gold

## Historical pool

- Discovered: 152221
- Ever alive: 27982
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
