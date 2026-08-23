# SyndProxy validated proxy pool

## Current pool

- Alive now: 468
- Gold now: 376
- HTTP: 88 alive / 58 gold
- HTTPS: 39 alive / 11 gold
- SOCKS4: 164 alive / 151 gold
- SOCKS5: 177 alive / 156 gold

## Historical pool

- Discovered: 174811
- Ever alive: 33099
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
