# SyndProxy validated proxy pool

## Current pool

- Alive now: 448
- Gold now: 365
- HTTP: 75 alive / 50 gold
- HTTPS: 27 alive / 15 gold
- SOCKS4: 167 alive / 154 gold
- SOCKS5: 179 alive / 146 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48313
- Ever gold: 1528

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
