# SyndProxy validated proxy pool

## Current pool

- Alive now: 461
- Gold now: 364
- HTTP: 82 alive / 49 gold
- HTTPS: 33 alive / 9 gold
- SOCKS4: 166 alive / 154 gold
- SOCKS5: 180 alive / 152 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48295
- Ever gold: 1527

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
