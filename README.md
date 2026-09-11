# SyndProxy validated proxy pool

## Current pool

- Alive now: 461
- Gold now: 363
- HTTP: 101 alive / 71 gold
- HTTPS: 56 alive / 22 gold
- SOCKS4: 121 alive / 100 gold
- SOCKS5: 183 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48712
- Ever gold: 1564

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
