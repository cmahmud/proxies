# SyndProxy private pool

## Current pool

- Alive now: 1431
- Gold now: 603
- HTTP: 554 alive / 192 gold
- HTTPS: 403 alive / 100 gold
- SOCKS4: 229 alive / 146 gold
- SOCKS5: 245 alive / 165 gold

## Historical pool

- Discovered: 138956
- Ever alive: 23410
- Ever gold: 920

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
