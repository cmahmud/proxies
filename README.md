# SyndProxy validated proxy pool

## Current pool

- Alive now: 466
- Gold now: 396
- HTTP: 88 alive / 65 gold
- HTTPS: 48 alive / 20 gold
- SOCKS4: 160 alive / 153 gold
- SOCKS5: 170 alive / 158 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43650
- Ever gold: 1375

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
