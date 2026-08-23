# SyndProxy validated proxy pool

## Current pool

- Alive now: 607
- Gold now: 342
- HTTP: 133 alive / 39 gold
- HTTPS: 93 alive / 8 gold
- SOCKS4: 179 alive / 151 gold
- SOCKS5: 202 alive / 144 gold

## Historical pool

- Discovered: 171094
- Ever alive: 32878
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
