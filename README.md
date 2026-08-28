# SyndProxy validated proxy pool

## Current pool

- Alive now: 640
- Gold now: 428
- HTTP: 121 alive / 80 gold
- HTTPS: 143 alive / 21 gold
- SOCKS4: 181 alive / 159 gold
- SOCKS5: 195 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42360
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
