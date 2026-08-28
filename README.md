# SyndProxy validated proxy pool

## Current pool

- Alive now: 620
- Gold now: 429
- HTTP: 113 alive / 79 gold
- HTTPS: 138 alive / 19 gold
- SOCKS4: 179 alive / 162 gold
- SOCKS5: 190 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42279
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
