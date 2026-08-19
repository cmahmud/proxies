# SyndProxy private pool

## Current pool

- Alive now: 1057
- Gold now: 362
- HTTP: 364 alive / 71 gold
- HTTPS: 250 alive / 19 gold
- SOCKS4: 214 alive / 121 gold
- SOCKS5: 229 alive / 151 gold

## Historical pool

- Discovered: 113527
- Ever alive: 16386
- Ever gold: 515

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
