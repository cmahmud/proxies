# SyndProxy validated proxy pool

## Current pool

- Alive now: 405
- Gold now: 354
- HTTP: 50 alive / 35 gold
- HTTPS: 25 alive / 4 gold
- SOCKS4: 160 alive / 153 gold
- SOCKS5: 170 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43563
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
