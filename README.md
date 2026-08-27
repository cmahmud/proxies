# SyndProxy validated proxy pool

## Current pool

- Alive now: 570
- Gold now: 416
- HTTP: 101 alive / 72 gold
- HTTPS: 115 alive / 19 gold
- SOCKS4: 170 alive / 160 gold
- SOCKS5: 184 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41927
- Ever gold: 1344

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
