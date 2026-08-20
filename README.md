# SyndProxy private pool

## Current pool

- Alive now: 1243
- Gold now: 593
- HTTP: 446 alive / 204 gold
- HTTPS: 328 alive / 101 gold
- SOCKS4: 213 alive / 137 gold
- SOCKS5: 256 alive / 151 gold

## Historical pool

- Discovered: 138948
- Ever alive: 23395
- Ever gold: 919

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
