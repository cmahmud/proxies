# SyndProxy private pool

## Current pool

- Alive now: 903
- Gold now: 229
- HTTP: 269 alive / 29 gold
- HTTPS: 156 alive / 8 gold
- SOCKS4: 253 alive / 110 gold
- SOCKS5: 225 alive / 82 gold

## Historical pool

- Discovered: 86774
- Ever alive: 7592
- Ever gold: 337

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
