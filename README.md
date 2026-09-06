# SyndProxy validated proxy pool

## Current pool

- Alive now: 466
- Gold now: 374
- HTTP: 87 alive / 56 gold
- HTTPS: 35 alive / 10 gold
- SOCKS4: 167 alive / 153 gold
- SOCKS5: 177 alive / 155 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48291
- Ever gold: 1527

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
