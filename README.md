# SyndProxy private pool

## Current pool

- Alive now: 979
- Gold now: 387
- HTTP: 293 alive / 75 gold
- HTTPS: 213 alive / 27 gold
- SOCKS4: 221 alive / 121 gold
- SOCKS5: 252 alive / 164 gold

## Historical pool

- Discovered: 164965
- Ever alive: 32245
- Ever gold: 1177

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
