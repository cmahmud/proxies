# SyndProxy private pool

## Current pool

- Alive now: 1030
- Gold now: 245
- HTTP: 387 alive / 26 gold
- HTTPS: 213 alive / 2 gold
- SOCKS4: 209 alive / 122 gold
- SOCKS5: 221 alive / 95 gold

## Historical pool

- Discovered: 95391
- Ever alive: 10602
- Ever gold: 378

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
