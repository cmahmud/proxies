# SyndProxy validated proxy pool

## Current pool

- Alive now: 363
- Gold now: 283
- HTTP: 40 alive / 25 gold
- HTTPS: 2 alive / 0 gold
- SOCKS4: 157 alive / 130 gold
- SOCKS5: 164 alive / 128 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43613
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
