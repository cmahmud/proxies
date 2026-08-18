# SyndProxy private pool

## Current pool

- Alive now: 887
- Gold now: 275
- HTTP: 284 alive / 32 gold
- HTTPS: 169 alive / 5 gold
- SOCKS4: 228 alive / 134 gold
- SOCKS5: 206 alive / 104 gold

## Historical pool

- Discovered: 99078
- Ever alive: 11452
- Ever gold: 382

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
