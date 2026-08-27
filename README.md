# SyndProxy validated proxy pool

## Current pool

- Alive now: 546
- Gold now: 415
- HTTP: 97 alive / 71 gold
- HTTPS: 104 alive / 23 gold
- SOCKS4: 168 alive / 159 gold
- SOCKS5: 177 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41960
- Ever gold: 1346

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
