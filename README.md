# SyndProxy private pool

## Current pool

- Alive now: 1057
- Gold now: 288
- HTTP: 320 alive / 29 gold
- HTTPS: 247 alive / 4 gold
- SOCKS4: 239 alive / 139 gold
- SOCKS5: 251 alive / 116 gold

## Historical pool

- Discovered: 101236
- Ever alive: 12670
- Ever gold: 399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
