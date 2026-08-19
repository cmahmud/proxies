# SyndProxy private pool

## Current pool

- Alive now: 1086
- Gold now: 336
- HTTP: 398 alive / 64 gold
- HTTPS: 275 alive / 17 gold
- SOCKS4: 186 alive / 113 gold
- SOCKS5: 227 alive / 142 gold

## Historical pool

- Discovered: 113527
- Ever alive: 16343
- Ever gold: 508

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
