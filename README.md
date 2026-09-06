# SyndProxy validated proxy pool

## Current pool

- Alive now: 451
- Gold now: 373
- HTTP: 80 alive / 57 gold
- HTTPS: 33 alive / 11 gold
- SOCKS4: 161 alive / 151 gold
- SOCKS5: 177 alive / 154 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48276
- Ever gold: 1527

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
