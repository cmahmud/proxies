# SyndProxy validated proxy pool

## Current pool

- Alive now: 559
- Gold now: 399
- HTTP: 95 alive / 59 gold
- HTTPS: 100 alive / 13 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 192 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39267
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
