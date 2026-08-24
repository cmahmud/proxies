# SyndProxy validated proxy pool

## Current pool

- Alive now: 521
- Gold now: 405
- HTTP: 106 alive / 62 gold
- HTTPS: 51 alive / 16 gold
- SOCKS4: 172 alive / 159 gold
- SOCKS5: 192 alive / 168 gold

## Historical pool

- Discovered: 181088
- Ever alive: 33680
- Ever gold: 1248

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
