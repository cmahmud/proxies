# SyndProxy validated proxy pool

## Current pool

- Alive now: 611
- Gold now: 433
- HTTP: 133 alive / 79 gold
- HTTPS: 98 alive / 21 gold
- SOCKS4: 188 alive / 162 gold
- SOCKS5: 192 alive / 171 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34456
- Ever gold: 1255

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
