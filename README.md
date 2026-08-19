# SyndProxy private pool

## Current pool

- Alive now: 1147
- Gold now: 388
- HTTP: 369 alive / 88 gold
- HTTPS: 223 alive / 15 gold
- SOCKS4: 252 alive / 145 gold
- SOCKS5: 303 alive / 140 gold

## Historical pool

- Discovered: 133967
- Ever alive: 21710
- Ever gold: 887

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
