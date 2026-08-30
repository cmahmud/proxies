# SyndProxy validated proxy pool

## Current pool

- Alive now: 510
- Gold now: 413
- HTTP: 118 alive / 78 gold
- HTTPS: 53 alive / 27 gold
- SOCKS4: 170 alive / 150 gold
- SOCKS5: 169 alive / 158 gold

## Historical pool

- Discovered: 199830
- Ever alive: 43704
- Ever gold: 1379

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
