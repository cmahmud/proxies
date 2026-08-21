# SyndProxy private pool

## Current pool

- Alive now: 954
- Gold now: 377
- HTTP: 296 alive / 82 gold
- HTTPS: 216 alive / 24 gold
- SOCKS4: 212 alive / 132 gold
- SOCKS5: 230 alive / 139 gold

## Historical pool

- Discovered: 155800
- Ever alive: 29369
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
