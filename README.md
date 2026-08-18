# SyndProxy private pool

## Current pool

- Alive now: 923
- Gold now: 344
- HTTP: 290 alive / 50 gold
- HTTPS: 166 alive / 15 gold
- SOCKS4: 234 alive / 140 gold
- SOCKS5: 233 alive / 139 gold

## Historical pool

- Discovered: 107067
- Ever alive: 14687
- Ever gold: 474

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
