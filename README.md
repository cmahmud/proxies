# SyndProxy private pool

## Current pool

- Alive now: 1767
- Gold now: 636
- HTTP: 730 alive / 238 gold
- HTTPS: 564 alive / 128 gold
- SOCKS4: 205 alive / 129 gold
- SOCKS5: 268 alive / 141 gold

## Historical pool

- Discovered: 142716
- Ever alive: 24505
- Ever gold: 1026

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
