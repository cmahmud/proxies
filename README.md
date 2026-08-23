# SyndProxy validated proxy pool

## Current pool

- Alive now: 466
- Gold now: 377
- HTTP: 88 alive / 60 gold
- HTTPS: 36 alive / 10 gold
- SOCKS4: 165 alive / 152 gold
- SOCKS5: 177 alive / 155 gold

## Historical pool

- Discovered: 174811
- Ever alive: 33098
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
