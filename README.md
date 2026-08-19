# SyndProxy private pool

## Current pool

- Alive now: 979
- Gold now: 377
- HTTP: 308 alive / 77 gold
- HTTPS: 213 alive / 13 gold
- SOCKS4: 229 alive / 135 gold
- SOCKS5: 229 alive / 152 gold

## Historical pool

- Discovered: 129304
- Ever alive: 20389
- Ever gold: 865

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
