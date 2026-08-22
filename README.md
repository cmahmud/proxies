# SyndProxy private pool

## Current pool

- Alive now: 947
- Gold now: 368
- HTTP: 309 alive / 79 gold
- HTTPS: 196 alive / 25 gold
- SOCKS4: 206 alive / 126 gold
- SOCKS5: 236 alive / 138 gold

## Historical pool

- Discovered: 165816
- Ever alive: 32321
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
