# SyndProxy private pool

## Current pool

- Alive now: 961
- Gold now: 374
- HTTP: 298 alive / 90 gold
- HTTPS: 215 alive / 25 gold
- SOCKS4: 216 alive / 134 gold
- SOCKS5: 232 alive / 125 gold

## Historical pool

- Discovered: 161993
- Ever alive: 31328
- Ever gold: 1157

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
