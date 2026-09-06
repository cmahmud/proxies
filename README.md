# SyndProxy validated proxy pool

## Current pool

- Alive now: 475
- Gold now: 386
- HTTP: 94 alive / 60 gold
- HTTPS: 28 alive / 14 gold
- SOCKS4: 170 alive / 153 gold
- SOCKS5: 183 alive / 159 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48240
- Ever gold: 1526

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
