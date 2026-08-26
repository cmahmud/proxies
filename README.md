# SyndProxy validated proxy pool

## Current pool

- Alive now: 534
- Gold now: 389
- HTTP: 99 alive / 67 gold
- HTTPS: 87 alive / 18 gold
- SOCKS4: 168 alive / 149 gold
- SOCKS5: 180 alive / 155 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39319
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
