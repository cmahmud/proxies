# SyndProxy validated proxy pool

## Current pool

- Alive now: 410
- Gold now: 309
- HTTP: 53 alive / 30 gold
- HTTPS: 28 alive / 5 gold
- SOCKS4: 160 alive / 141 gold
- SOCKS5: 169 alive / 133 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43589
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
