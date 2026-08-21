# SyndProxy private pool

## Current pool

- Alive now: 1055
- Gold now: 418
- HTTP: 348 alive / 92 gold
- HTTPS: 228 alive / 23 gold
- SOCKS4: 218 alive / 148 gold
- SOCKS5: 261 alive / 155 gold

## Historical pool

- Discovered: 156426
- Ever alive: 29514
- Ever gold: 1129

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
