# SyndProxy validated proxy pool

## Current pool

- Alive now: 580
- Gold now: 454
- HTTP: 94 alive / 77 gold
- HTTPS: 111 alive / 36 gold
- SOCKS4: 180 alive / 162 gold
- SOCKS5: 195 alive / 179 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47397
- Ever gold: 1468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
