# SyndProxy validated proxy pool

## Current pool

- Alive now: 431
- Gold now: 350
- HTTP: 58 alive / 45 gold
- HTTPS: 42 alive / 7 gold
- SOCKS4: 163 alive / 147 gold
- SOCKS5: 168 alive / 151 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43534
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
