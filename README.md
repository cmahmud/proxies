# SyndProxy private pool

## Current pool

- Alive now: 1046
- Gold now: 406
- HTTP: 379 alive / 93 gold
- HTTPS: 228 alive / 29 gold
- SOCKS4: 212 alive / 139 gold
- SOCKS5: 227 alive / 145 gold

## Historical pool

- Discovered: 163252
- Ever alive: 31744
- Ever gold: 1165

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
