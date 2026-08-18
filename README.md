# SyndProxy private pool

## Current pool

- Alive now: 851
- Gold now: 321
- HTTP: 247 alive / 39 gold
- HTTPS: 171 alive / 9 gold
- SOCKS4: 209 alive / 140 gold
- SOCKS5: 224 alive / 133 gold

## Historical pool

- Discovered: 102931
- Ever alive: 13985
- Ever gold: 435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
