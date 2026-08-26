# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 407
- HTTP: 105 alive / 67 gold
- HTTPS: 85 alive / 19 gold
- SOCKS4: 174 alive / 159 gold
- SOCKS5: 172 alive / 162 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37748
- Ever gold: 1287

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
