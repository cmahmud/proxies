# SyndProxy private pool

## Current pool

- Alive now: 1782
- Gold now: 644
- HTTP: 749 alive / 243 gold
- HTTPS: 590 alive / 129 gold
- SOCKS4: 208 alive / 132 gold
- SOCKS5: 235 alive / 140 gold

## Historical pool

- Discovered: 142716
- Ever alive: 24513
- Ever gold: 1026

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
