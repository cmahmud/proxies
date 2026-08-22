# SyndProxy private pool

## Current pool

- Alive now: 1047
- Gold now: 399
- HTTP: 357 alive / 84 gold
- HTTPS: 214 alive / 26 gold
- SOCKS4: 227 alive / 133 gold
- SOCKS5: 249 alive / 156 gold

## Historical pool

- Discovered: 166609
- Ever alive: 32418
- Ever gold: 1180

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
