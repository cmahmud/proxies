# SyndProxy private pool

## Current pool

- Alive now: 1331
- Gold now: 598
- HTTP: 508 alive / 183 gold
- HTTPS: 351 alive / 112 gold
- SOCKS4: 243 alive / 145 gold
- SOCKS5: 229 alive / 158 gold

## Historical pool

- Discovered: 125593
- Ever alive: 19553
- Ever gold: 772

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
