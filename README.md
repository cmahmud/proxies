# SyndProxy validated proxy pool

## Current pool

- Alive now: 626
- Gold now: 433
- HTTP: 112 alive / 82 gold
- HTTPS: 142 alive / 20 gold
- SOCKS4: 180 alive / 161 gold
- SOCKS5: 192 alive / 170 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42278
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
