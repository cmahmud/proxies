# SyndProxy private pool

## Current pool

- Alive now: 1033
- Gold now: 340
- HTTP: 401 alive / 49 gold
- HTTPS: 186 alive / 9 gold
- SOCKS4: 228 alive / 143 gold
- SOCKS5: 218 alive / 139 gold

## Historical pool

- Discovered: 107060
- Ever alive: 14636
- Ever gold: 467

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
