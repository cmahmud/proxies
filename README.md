# SyndProxy validated proxy pool

## Current pool

- Alive now: 458
- Gold now: 388
- HTTP: 89 alive / 61 gold
- HTTPS: 46 alive / 20 gold
- SOCKS4: 159 alive / 153 gold
- SOCKS5: 164 alive / 154 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43647
- Ever gold: 1375

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
