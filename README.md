# SyndProxy private pool

## Current pool

- Alive now: 1228
- Gold now: 409
- HTTP: 419 alive / 91 gold
- HTTPS: 280 alive / 18 gold
- SOCKS4: 243 alive / 141 gold
- SOCKS5: 286 alive / 159 gold

## Historical pool

- Discovered: 131817
- Ever alive: 20866
- Ever gold: 876

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
