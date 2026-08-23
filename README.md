# SyndProxy validated proxy pool

## Current pool

- Alive now: 477
- Gold now: 375
- HTTP: 89 alive / 57 gold
- HTTPS: 34 alive / 12 gold
- SOCKS4: 167 alive / 150 gold
- SOCKS5: 187 alive / 156 gold

## Historical pool

- Discovered: 174811
- Ever alive: 33099
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
