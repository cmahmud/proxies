# SyndProxy private pool

## Current pool

- Alive now: 1080
- Gold now: 392
- HTTP: 347 alive / 87 gold
- HTTPS: 249 alive / 19 gold
- SOCKS4: 229 alive / 147 gold
- SOCKS5: 255 alive / 139 gold

## Historical pool

- Discovered: 158238
- Ever alive: 30000
- Ever gold: 1139

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
