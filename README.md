# SyndProxy private pool

## Current pool

- Alive now: 1036
- Gold now: 478
- HTTP: 338 alive / 144 gold
- HTTPS: 267 alive / 87 gold
- SOCKS4: 209 alive / 118 gold
- SOCKS5: 222 alive / 129 gold

## Historical pool

- Discovered: 117156
- Ever alive: 17572
- Ever gold: 690

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
