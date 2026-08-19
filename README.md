# SyndProxy private pool

## Current pool

- Alive now: 1274
- Gold now: 403
- HTTP: 428 alive / 92 gold
- HTTPS: 319 alive / 20 gold
- SOCKS4: 232 alive / 139 gold
- SOCKS5: 295 alive / 152 gold

## Historical pool

- Discovered: 135758
- Ever alive: 22201
- Ever gold: 893

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
