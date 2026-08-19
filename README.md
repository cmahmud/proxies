# SyndProxy private pool

## Current pool

- Alive now: 1148
- Gold now: 412
- HTTP: 405 alive / 95 gold
- HTTPS: 249 alive / 17 gold
- SOCKS4: 233 alive / 142 gold
- SOCKS5: 261 alive / 158 gold

## Historical pool

- Discovered: 131817
- Ever alive: 20894
- Ever gold: 876

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
