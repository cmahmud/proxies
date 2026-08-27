# SyndProxy validated proxy pool

## Current pool

- Alive now: 557
- Gold now: 418
- HTTP: 97 alive / 76 gold
- HTTPS: 112 alive / 23 gold
- SOCKS4: 168 alive / 158 gold
- SOCKS5: 180 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41846
- Ever gold: 1344

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
