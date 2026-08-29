# SyndProxy validated proxy pool

## Current pool

- Alive now: 376
- Gold now: 323
- HTTP: 44 alive / 30 gold
- HTTPS: 11 alive / 0 gold
- SOCKS4: 158 alive / 138 gold
- SOCKS5: 163 alive / 155 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43607
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
