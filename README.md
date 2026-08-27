# SyndProxy validated proxy pool

## Current pool

- Alive now: 569
- Gold now: 415
- HTTP: 102 alive / 74 gold
- HTTPS: 112 alive / 17 gold
- SOCKS4: 175 alive / 159 gold
- SOCKS5: 180 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42070
- Ever gold: 1348

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
