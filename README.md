# SyndProxy private pool

## Current pool

- Alive now: 1717
- Gold now: 642
- HTTP: 701 alive / 239 gold
- HTTPS: 552 alive / 129 gold
- SOCKS4: 208 alive / 133 gold
- SOCKS5: 256 alive / 141 gold

## Historical pool

- Discovered: 142716
- Ever alive: 24505
- Ever gold: 1026

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
