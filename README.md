# SyndProxy private pool

## Current pool

- Alive now: 1735
- Gold now: 660
- HTTP: 720 alive / 241 gold
- HTTPS: 562 alive / 141 gold
- SOCKS4: 211 alive / 135 gold
- SOCKS5: 242 alive / 143 gold

## Historical pool

- Discovered: 142719
- Ever alive: 24527
- Ever gold: 1026

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
