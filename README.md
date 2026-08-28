# SyndProxy validated proxy pool

## Current pool

- Alive now: 501
- Gold now: 385
- HTTP: 96 alive / 67 gold
- HTTPS: 70 alive / 9 gold
- SOCKS4: 162 alive / 153 gold
- SOCKS5: 173 alive / 156 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43172
- Ever gold: 1366

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
