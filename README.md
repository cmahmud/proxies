# SyndProxy validated proxy pool

## Current pool

- Alive now: 399
- Gold now: 353
- HTTP: 54 alive / 34 gold
- HTTPS: 18 alive / 4 gold
- SOCKS4: 159 alive / 156 gold
- SOCKS5: 168 alive / 159 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43593
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
