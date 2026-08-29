# SyndProxy validated proxy pool

## Current pool

- Alive now: 399
- Gold now: 319
- HTTP: 52 alive / 29 gold
- HTTPS: 20 alive / 2 gold
- SOCKS4: 159 alive / 150 gold
- SOCKS5: 168 alive / 138 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43591
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
