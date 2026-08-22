# SyndProxy private pool

## Current pool

- Alive now: 972
- Gold now: 367
- HTTP: 310 alive / 78 gold
- HTTPS: 232 alive / 23 gold
- SOCKS4: 200 alive / 125 gold
- SOCKS5: 230 alive / 141 gold

## Historical pool

- Discovered: 165812
- Ever alive: 32318
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
