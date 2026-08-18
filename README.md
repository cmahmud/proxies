# SyndProxy private pool

## Current pool

- Alive now: 974
- Gold now: 244
- HTTP: 364 alive / 27 gold
- HTTPS: 189 alive / 1 gold
- SOCKS4: 202 alive / 122 gold
- SOCKS5: 219 alive / 94 gold

## Historical pool

- Discovered: 95388
- Ever alive: 10585
- Ever gold: 377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
