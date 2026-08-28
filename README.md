# SyndProxy validated proxy pool

## Current pool

- Alive now: 560
- Gold now: 418
- HTTP: 94 alive / 69 gold
- HTTPS: 107 alive / 20 gold
- SOCKS4: 177 alive / 160 gold
- SOCKS5: 182 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42563
- Ever gold: 1358

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
