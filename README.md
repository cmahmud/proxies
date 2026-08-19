# SyndProxy private pool

## Current pool

- Alive now: 1080
- Gold now: 398
- HTTP: 344 alive / 71 gold
- HTTPS: 249 alive / 19 gold
- SOCKS4: 234 alive / 144 gold
- SOCKS5: 253 alive / 164 gold

## Historical pool

- Discovered: 113527
- Ever alive: 16387
- Ever gold: 515

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
