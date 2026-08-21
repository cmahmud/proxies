# SyndProxy private pool

## Current pool

- Alive now: 938
- Gold now: 398
- HTTP: 298 alive / 88 gold
- HTTPS: 181 alive / 23 gold
- SOCKS4: 228 alive / 148 gold
- SOCKS5: 231 alive / 139 gold

## Historical pool

- Discovered: 155800
- Ever alive: 29374
- Ever gold: 1126

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
