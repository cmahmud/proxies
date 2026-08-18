# SyndProxy private pool

## Current pool

- Alive now: 963
- Gold now: 350
- HTTP: 281 alive / 51 gold
- HTTPS: 201 alive / 14 gold
- SOCKS4: 246 alive / 147 gold
- SOCKS5: 235 alive / 138 gold

## Historical pool

- Discovered: 107085
- Ever alive: 14721
- Ever gold: 474

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
