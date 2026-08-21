# SyndProxy private pool

## Current pool

- Alive now: 951
- Gold now: 403
- HTTP: 308 alive / 106 gold
- HTTPS: 228 alive / 30 gold
- SOCKS4: 205 alive / 147 gold
- SOCKS5: 210 alive / 120 gold

## Historical pool

- Discovered: 153184
- Ever alive: 28476
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
