# SyndProxy validated proxy pool

## Current pool

- Alive now: 434
- Gold now: 366
- HTTP: 70 alive / 52 gold
- HTTPS: 29 alive / 13 gold
- SOCKS4: 163 alive / 150 gold
- SOCKS5: 172 alive / 151 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48260
- Ever gold: 1527

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
