# SyndProxy private pool

## Current pool

- Alive now: 1804
- Gold now: 644
- HTTP: 759 alive / 243 gold
- HTTPS: 603 alive / 129 gold
- SOCKS4: 207 alive / 132 gold
- SOCKS5: 235 alive / 140 gold

## Historical pool

- Discovered: 142716
- Ever alive: 24514
- Ever gold: 1026

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
