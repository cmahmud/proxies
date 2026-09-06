# SyndProxy validated proxy pool

## Current pool

- Alive now: 461
- Gold now: 369
- HTTP: 78 alive / 54 gold
- HTTPS: 31 alive / 11 gold
- SOCKS4: 170 alive / 150 gold
- SOCKS5: 182 alive / 154 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48270
- Ever gold: 1527

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
