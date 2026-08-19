# SyndProxy private pool

## Current pool

- Alive now: 1027
- Gold now: 515
- HTTP: 370 alive / 152 gold
- HTTPS: 246 alive / 90 gold
- SOCKS4: 206 alive / 133 gold
- SOCKS5: 205 alive / 140 gold

## Historical pool

- Discovered: 127357
- Ever alive: 19892
- Ever gold: 803

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
