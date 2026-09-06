# SyndProxy validated proxy pool

## Current pool

- Alive now: 479
- Gold now: 395
- HTTP: 103 alive / 75 gold
- HTTPS: 44 alive / 17 gold
- SOCKS4: 162 alive / 150 gold
- SOCKS5: 170 alive / 153 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48206
- Ever gold: 1524

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
