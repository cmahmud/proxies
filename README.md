# SyndProxy validated proxy pool

## Current pool

- Alive now: 499
- Gold now: 390
- HTTP: 113 alive / 62 gold
- HTTPS: 42 alive / 14 gold
- SOCKS4: 165 alive / 155 gold
- SOCKS5: 179 alive / 159 gold

## Historical pool

- Discovered: 175416
- Ever alive: 33127
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
