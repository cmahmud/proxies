# SyndProxy private pool

## Current pool

- Alive now: 1201
- Gold now: 388
- HTTP: 392 alive / 92 gold
- HTTPS: 268 alive / 19 gold
- SOCKS4: 243 alive / 137 gold
- SOCKS5: 298 alive / 140 gold

## Historical pool

- Discovered: 133961
- Ever alive: 21621
- Ever gold: 886

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
