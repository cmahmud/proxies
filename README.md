# SyndProxy validated proxy pool

## Current pool

- Alive now: 715
- Gold now: 473
- HTTP: 177 alive / 97 gold
- HTTPS: 127 alive / 38 gold
- SOCKS4: 180 alive / 162 gold
- SOCKS5: 231 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45296
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
