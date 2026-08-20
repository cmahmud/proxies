# SyndProxy private pool

## Current pool

- Alive now: 1415
- Gold now: 577
- HTTP: 512 alive / 215 gold
- HTTPS: 360 alive / 73 gold
- SOCKS4: 211 alive / 124 gold
- SOCKS5: 332 alive / 165 gold

## Historical pool

- Discovered: 143496
- Ever alive: 24841
- Ever gold: 1050

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
