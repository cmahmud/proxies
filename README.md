# SyndProxy private pool

## Current pool

- Alive now: 1400
- Gold now: 419
- HTTP: 517 alive / 86 gold
- HTTPS: 353 alive / 18 gold
- SOCKS4: 260 alive / 156 gold
- SOCKS5: 270 alive / 159 gold

## Historical pool

- Discovered: 131814
- Ever alive: 20841
- Ever gold: 876

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
