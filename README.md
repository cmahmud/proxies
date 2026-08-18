# SyndProxy private pool

## Current pool

- Alive now: 1036
- Gold now: 239
- HTTP: 364 alive / 30 gold
- HTTPS: 175 alive / 8 gold
- SOCKS4: 279 alive / 115 gold
- SOCKS5: 218 alive / 86 gold

## Historical pool

- Discovered: 86712
- Ever alive: 6879
- Ever gold: 318

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
