# SyndProxy validated proxy pool

## Current pool

- Alive now: 587
- Gold now: 436
- HTTP: 130 alive / 81 gold
- HTTPS: 81 alive / 23 gold
- SOCKS4: 187 alive / 161 gold
- SOCKS5: 189 alive / 171 gold

## Historical pool

- Discovered: 181494
- Ever alive: 33962
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
