# SyndProxy private pool

## Current pool

- Alive now: 1232
- Gold now: 410
- HTTP: 452 alive / 92 gold
- HTTPS: 258 alive / 18 gold
- SOCKS4: 237 alive / 141 gold
- SOCKS5: 285 alive / 159 gold

## Historical pool

- Discovered: 131817
- Ever alive: 20866
- Ever gold: 876

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
