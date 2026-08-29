# SyndProxy validated proxy pool

## Current pool

- Alive now: 367
- Gold now: 319
- HTTP: 53 alive / 31 gold
- HTTPS: 13 alive / 0 gold
- SOCKS4: 148 alive / 144 gold
- SOCKS5: 153 alive / 144 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43632
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
