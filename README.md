# SyndProxy private pool

## Current pool

- Alive now: 953
- Gold now: 408
- HTTP: 342 alive / 90 gold
- HTTPS: 184 alive / 32 gold
- SOCKS4: 205 alive / 147 gold
- SOCKS5: 222 alive / 139 gold

## Historical pool

- Discovered: 167118
- Ever alive: 32530
- Ever gold: 1185

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
