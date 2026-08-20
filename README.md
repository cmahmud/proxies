# SyndProxy private pool

## Current pool

- Alive now: 1771
- Gold now: 642
- HTTP: 742 alive / 242 gold
- HTTPS: 575 alive / 129 gold
- SOCKS4: 210 alive / 132 gold
- SOCKS5: 244 alive / 139 gold

## Historical pool

- Discovered: 142716
- Ever alive: 24507
- Ever gold: 1026

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
