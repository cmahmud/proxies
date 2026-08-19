# SyndProxy private pool

## Current pool

- Alive now: 1233
- Gold now: 387
- HTTP: 415 alive / 90 gold
- HTTPS: 286 alive / 19 gold
- SOCKS4: 235 alive / 137 gold
- SOCKS5: 297 alive / 141 gold

## Historical pool

- Discovered: 133962
- Ever alive: 21645
- Ever gold: 886

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
