# SyndProxy private pool

## Current pool

- Alive now: 998
- Gold now: 304
- HTTP: 389 alive / 30 gold
- HTTPS: 182 alive / 6 gold
- SOCKS4: 218 alive / 141 gold
- SOCKS5: 209 alive / 127 gold

## Historical pool

- Discovered: 102848
- Ever alive: 13392
- Ever gold: 415

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
