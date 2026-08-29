# SyndProxy validated proxy pool

## Current pool

- Alive now: 355
- Gold now: 233
- HTTP: 37 alive / 23 gold
- HTTPS: 5 alive / 0 gold
- SOCKS4: 154 alive / 110 gold
- SOCKS5: 159 alive / 100 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43619
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
