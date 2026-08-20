# SyndProxy private pool

## Current pool

- Alive now: 1680
- Gold now: 645
- HTTP: 693 alive / 240 gold
- HTTPS: 533 alive / 129 gold
- SOCKS4: 208 alive / 133 gold
- SOCKS5: 246 alive / 143 gold

## Historical pool

- Discovered: 142719
- Ever alive: 24527
- Ever gold: 1026

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
