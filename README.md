# SyndProxy validated proxy pool

## Current pool

- Alive now: 566
- Gold now: 431
- HTTP: 133 alive / 81 gold
- HTTPS: 71 alive / 21 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 190 alive / 168 gold

## Historical pool

- Discovered: 181494
- Ever alive: 33949
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
