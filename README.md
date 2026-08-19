# SyndProxy private pool

## Current pool

- Alive now: 1133
- Gold now: 417
- HTTP: 339 alive / 88 gold
- HTTPS: 274 alive / 24 gold
- SOCKS4: 227 alive / 146 gold
- SOCKS5: 293 alive / 159 gold

## Historical pool

- Discovered: 136206
- Ever alive: 22354
- Ever gold: 898

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
