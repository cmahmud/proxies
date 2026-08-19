# SyndProxy private pool

## Current pool

- Alive now: 1106
- Gold now: 533
- HTTP: 401 alive / 161 gold
- HTTPS: 268 alive / 84 gold
- SOCKS4: 233 alive / 150 gold
- SOCKS5: 204 alive / 138 gold

## Historical pool

- Discovered: 119814
- Ever alive: 18042
- Ever gold: 713

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
