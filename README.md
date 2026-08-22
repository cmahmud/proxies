# SyndProxy private pool

## Current pool

- Alive now: 865
- Gold now: 434
- HTTP: 225 alive / 92 gold
- HTTPS: 152 alive / 30 gold
- SOCKS4: 227 alive / 153 gold
- SOCKS5: 261 alive / 159 gold

## Historical pool

- Discovered: 163285
- Ever alive: 31818
- Ever gold: 1167

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
