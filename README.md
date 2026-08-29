# SyndProxy validated proxy pool

## Current pool

- Alive now: 415
- Gold now: 332
- HTTP: 51 alive / 33 gold
- HTTPS: 30 alive / 6 gold
- SOCKS4: 160 alive / 148 gold
- SOCKS5: 174 alive / 145 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43572
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
