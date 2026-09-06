# SyndProxy validated proxy pool

## Current pool

- Alive now: 460
- Gold now: 371
- HTTP: 80 alive / 55 gold
- HTTPS: 29 alive / 13 gold
- SOCKS4: 169 alive / 150 gold
- SOCKS5: 182 alive / 153 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48263
- Ever gold: 1527

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
