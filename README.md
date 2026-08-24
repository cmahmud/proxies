# SyndProxy validated proxy pool

## Current pool

- Alive now: 570
- Gold now: 436
- HTTP: 133 alive / 83 gold
- HTTPS: 80 alive / 22 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 188 alive / 170 gold

## Historical pool

- Discovered: 181494
- Ever alive: 33985
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
