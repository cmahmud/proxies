# SyndProxy private pool

## Current pool

- Alive now: 1201
- Gold now: 399
- HTTP: 392 alive / 90 gold
- HTTPS: 252 alive / 17 gold
- SOCKS4: 241 alive / 146 gold
- SOCKS5: 316 alive / 146 gold

## Historical pool

- Discovered: 133967
- Ever alive: 21742
- Ever gold: 887

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
