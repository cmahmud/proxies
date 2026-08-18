# SyndProxy private pool

## Current pool

- Alive now: 924
- Gold now: 278
- HTTP: 300 alive / 33 gold
- HTTPS: 188 alive / 4 gold
- SOCKS4: 225 alive / 136 gold
- SOCKS5: 211 alive / 105 gold

## Historical pool

- Discovered: 99076
- Ever alive: 11410
- Ever gold: 382

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
