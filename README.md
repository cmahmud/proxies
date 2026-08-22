# SyndProxy private pool

## Current pool

- Alive now: 1006
- Gold now: 371
- HTTP: 336 alive / 78 gold
- HTTPS: 238 alive / 23 gold
- SOCKS4: 205 alive / 126 gold
- SOCKS5: 227 alive / 144 gold

## Historical pool

- Discovered: 165812
- Ever alive: 32318
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
