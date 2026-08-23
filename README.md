# SyndProxy validated proxy pool

## Current pool

- Alive now: 575
- Gold now: 386
- HTTP: 125 alive / 65 gold
- HTTPS: 75 alive / 10 gold
- SOCKS4: 180 alive / 153 gold
- SOCKS5: 195 alive / 158 gold

## Historical pool

- Discovered: 175427
- Ever alive: 33144
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
