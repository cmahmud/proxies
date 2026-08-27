# SyndProxy validated proxy pool

## Current pool

- Alive now: 645
- Gold now: 405
- HTTP: 124 alive / 62 gold
- HTTPS: 162 alive / 13 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 190 alive / 170 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40866
- Ever gold: 1313

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
