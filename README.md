# SyndProxy private pool

## Current pool

- Alive now: 1760
- Gold now: 654
- HTTP: 737 alive / 239 gold
- HTTPS: 585 alive / 141 gold
- SOCKS4: 208 alive / 134 gold
- SOCKS5: 230 alive / 140 gold

## Historical pool

- Discovered: 142719
- Ever alive: 24520
- Ever gold: 1026

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
