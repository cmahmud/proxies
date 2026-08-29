# SyndProxy validated proxy pool

## Current pool

- Alive now: 389
- Gold now: 293
- HTTP: 47 alive / 31 gold
- HTTPS: 16 alive / 4 gold
- SOCKS4: 159 alive / 131 gold
- SOCKS5: 167 alive / 127 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43589
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
