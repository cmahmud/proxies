# SyndProxy private pool

## Current pool

- Alive now: 1166
- Gold now: 464
- HTTP: 433 alive / 124 gold
- HTTPS: 308 alive / 74 gold
- SOCKS4: 218 alive / 139 gold
- SOCKS5: 207 alive / 127 gold

## Historical pool

- Discovered: 113565
- Ever alive: 16713
- Ever gold: 621

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
