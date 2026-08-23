# SyndProxy validated proxy pool

## Current pool

- Alive now: 495
- Gold now: 373
- HTTP: 100 alive / 56 gold
- HTTPS: 39 alive / 12 gold
- SOCKS4: 170 alive / 151 gold
- SOCKS5: 186 alive / 154 gold

## Historical pool

- Discovered: 174129
- Ever alive: 33058
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
