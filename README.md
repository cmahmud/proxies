# SyndProxy validated proxy pool

## Current pool

- Alive now: 475
- Gold now: 384
- HTTP: 93 alive / 58 gold
- HTTPS: 29 alive / 14 gold
- SOCKS4: 168 alive / 153 gold
- SOCKS5: 185 alive / 159 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48241
- Ever gold: 1526

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
