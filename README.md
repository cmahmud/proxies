# SyndProxy private pool

## Current pool

- Alive now: 917
- Gold now: 407
- HTTP: 268 alive / 89 gold
- HTTPS: 179 alive / 30 gold
- SOCKS4: 236 alive / 150 gold
- SOCKS5: 234 alive / 138 gold

## Historical pool

- Discovered: 161993
- Ever alive: 31322
- Ever gold: 1156

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
