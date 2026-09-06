# SyndProxy validated proxy pool

## Current pool

- Alive now: 433
- Gold now: 360
- HTTP: 75 alive / 53 gold
- HTTPS: 25 alive / 12 gold
- SOCKS4: 160 alive / 150 gold
- SOCKS5: 173 alive / 145 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48258
- Ever gold: 1527

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
