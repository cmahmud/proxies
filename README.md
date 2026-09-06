# SyndProxy validated proxy pool

## Current pool

- Alive now: 453
- Gold now: 364
- HTTP: 79 alive / 44 gold
- HTTPS: 30 alive / 11 gold
- SOCKS4: 166 alive / 156 gold
- SOCKS5: 178 alive / 153 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48308
- Ever gold: 1527

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
