# SyndProxy validated proxy pool

## Current pool

- Alive now: 464
- Gold now: 373
- HTTP: 66 alive / 49 gold
- HTTPS: 60 alive / 13 gold
- SOCKS4: 166 alive / 154 gold
- SOCKS5: 172 alive / 157 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43511
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
