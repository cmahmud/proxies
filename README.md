# SyndProxy validated proxy pool

## Current pool

- Alive now: 448
- Gold now: 362
- HTTP: 76 alive / 47 gold
- HTTPS: 31 alive / 11 gold
- SOCKS4: 159 alive / 152 gold
- SOCKS5: 182 alive / 152 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48302
- Ever gold: 1527

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
