# SyndProxy private pool

## Current pool

- Alive now: 931
- Gold now: 381
- HTTP: 255 alive / 87 gold
- HTTPS: 240 alive / 26 gold
- SOCKS4: 200 alive / 121 gold
- SOCKS5: 236 alive / 147 gold

## Historical pool

- Discovered: 164184
- Ever alive: 32058
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
