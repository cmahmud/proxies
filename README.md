# SyndProxy private pool

## Current pool

- Alive now: 1317
- Gold now: 415
- HTTP: 483 alive / 84 gold
- HTTPS: 301 alive / 15 gold
- SOCKS4: 272 alive / 157 gold
- SOCKS5: 261 alive / 159 gold

## Historical pool

- Discovered: 131814
- Ever alive: 20805
- Ever gold: 875

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
