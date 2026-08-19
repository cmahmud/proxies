# SyndProxy private pool

## Current pool

- Alive now: 1107
- Gold now: 335
- HTTP: 416 alive / 65 gold
- HTTPS: 276 alive / 17 gold
- SOCKS4: 186 alive / 110 gold
- SOCKS5: 229 alive / 143 gold

## Historical pool

- Discovered: 113527
- Ever alive: 16342
- Ever gold: 508

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
