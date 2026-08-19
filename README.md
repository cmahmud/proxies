# SyndProxy private pool

## Current pool

- Alive now: 1194
- Gold now: 466
- HTTP: 427 alive / 120 gold
- HTTPS: 286 alive / 72 gold
- SOCKS4: 238 alive / 141 gold
- SOCKS5: 243 alive / 133 gold

## Historical pool

- Discovered: 113536
- Ever alive: 16519
- Ever gold: 621

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
