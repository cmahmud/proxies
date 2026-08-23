# SyndProxy validated proxy pool

## Current pool

- Alive now: 484
- Gold now: 375
- HTTP: 89 alive / 58 gold
- HTTPS: 45 alive / 11 gold
- SOCKS4: 165 alive / 151 gold
- SOCKS5: 185 alive / 155 gold

## Historical pool

- Discovered: 174811
- Ever alive: 33101
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
