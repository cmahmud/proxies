# SyndProxy private pool

## Current pool

- Alive now: 1032
- Gold now: 304
- HTTP: 354 alive / 60 gold
- HTTPS: 265 alive / 19 gold
- SOCKS4: 214 alive / 118 gold
- SOCKS5: 199 alive / 107 gold

## Historical pool

- Discovered: 109987
- Ever alive: 15593
- Ever gold: 497

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
