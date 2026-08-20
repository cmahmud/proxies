# SyndProxy private pool

## Current pool

- Alive now: 849
- Gold now: 383
- HTTP: 213 alive / 78 gold
- HTTPS: 210 alive / 16 gold
- SOCKS4: 213 alive / 150 gold
- SOCKS5: 213 alive / 139 gold

## Historical pool

- Discovered: 149510
- Ever alive: 26871
- Ever gold: 1088

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
