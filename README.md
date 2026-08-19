# SyndProxy private pool

## Current pool

- Alive now: 996
- Gold now: 346
- HTTP: 341 alive / 72 gold
- HTTPS: 223 alive / 15 gold
- SOCKS4: 197 alive / 112 gold
- SOCKS5: 235 alive / 147 gold

## Historical pool

- Discovered: 113527
- Ever alive: 16384
- Ever gold: 515

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
