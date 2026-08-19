# SyndProxy private pool

## Current pool

- Alive now: 1087
- Gold now: 339
- HTTP: 396 alive / 65 gold
- HTTPS: 269 alive / 17 gold
- SOCKS4: 190 alive / 113 gold
- SOCKS5: 232 alive / 144 gold

## Historical pool

- Discovered: 113527
- Ever alive: 16346
- Ever gold: 508

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
