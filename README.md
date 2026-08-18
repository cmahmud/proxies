# SyndProxy private pool

## Current pool

- Alive now: 938
- Gold now: 344
- HTTP: 295 alive / 50 gold
- HTTPS: 177 alive / 15 gold
- SOCKS4: 232 alive / 140 gold
- SOCKS5: 234 alive / 139 gold

## Historical pool

- Discovered: 107067
- Ever alive: 14687
- Ever gold: 474

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
