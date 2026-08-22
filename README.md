# SyndProxy private pool

## Current pool

- Alive now: 1100
- Gold now: 426
- HTTP: 321 alive / 94 gold
- HTTPS: 234 alive / 25 gold
- SOCKS4: 239 alive / 139 gold
- SOCKS5: 306 alive / 168 gold

## Historical pool

- Discovered: 164947
- Ever alive: 32219
- Ever gold: 1174

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
