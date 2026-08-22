# SyndProxy private pool

## Current pool

- Alive now: 1053
- Gold now: 375
- HTTP: 358 alive / 80 gold
- HTTPS: 274 alive / 24 gold
- SOCKS4: 200 alive / 127 gold
- SOCKS5: 221 alive / 144 gold

## Historical pool

- Discovered: 165812
- Ever alive: 32318
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
