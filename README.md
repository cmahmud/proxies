# SyndProxy private pool

## Current pool

- Alive now: 991
- Gold now: 257
- HTTP: 411 alive / 30 gold
- HTTPS: 150 alive / 2 gold
- SOCKS4: 203 alive / 119 gold
- SOCKS5: 227 alive / 106 gold

## Historical pool

- Discovered: 99105
- Ever alive: 11747
- Ever gold: 389

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
