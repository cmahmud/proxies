# SyndProxy private pool

## Current pool

- Alive now: 880
- Gold now: 401
- HTTP: 271 alive / 90 gold
- HTTPS: 185 alive / 31 gold
- SOCKS4: 202 alive / 141 gold
- SOCKS5: 222 alive / 139 gold

## Historical pool

- Discovered: 163262
- Ever alive: 31780
- Ever gold: 1166

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
