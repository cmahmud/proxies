# SyndProxy private pool

## Current pool

- Alive now: 942
- Gold now: 368
- HTTP: 297 alive / 77 gold
- HTTPS: 198 alive / 26 gold
- SOCKS4: 214 alive / 126 gold
- SOCKS5: 233 alive / 139 gold

## Historical pool

- Discovered: 165816
- Ever alive: 32322
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
