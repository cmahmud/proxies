# SyndProxy private pool

## Current pool

- Alive now: 1050
- Gold now: 415
- HTTP: 344 alive / 87 gold
- HTTPS: 240 alive / 27 gold
- SOCKS4: 228 alive / 144 gold
- SOCKS5: 238 alive / 157 gold

## Historical pool

- Discovered: 159211
- Ever alive: 30196
- Ever gold: 1143

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
