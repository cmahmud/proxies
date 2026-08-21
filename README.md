# SyndProxy private pool

## Current pool

- Alive now: 908
- Gold now: 411
- HTTP: 273 alive / 85 gold
- HTTPS: 185 alive / 22 gold
- SOCKS4: 212 alive / 143 gold
- SOCKS5: 238 alive / 161 gold

## Historical pool

- Discovered: 156413
- Ever alive: 29437
- Ever gold: 1127

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
