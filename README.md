# SyndProxy private pool

## Current pool

- Alive now: 970
- Gold now: 279
- HTTP: 313 alive / 34 gold
- HTTPS: 215 alive / 4 gold
- SOCKS4: 229 alive / 136 gold
- SOCKS5: 213 alive / 105 gold

## Historical pool

- Discovered: 99076
- Ever alive: 11410
- Ever gold: 382

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
