# SyndProxy private pool

## Current pool

- Alive now: 892
- Gold now: 274
- HTTP: 279 alive / 34 gold
- HTTPS: 172 alive / 5 gold
- SOCKS4: 231 alive / 131 gold
- SOCKS5: 210 alive / 104 gold

## Historical pool

- Discovered: 99078
- Ever alive: 11452
- Ever gold: 382

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
