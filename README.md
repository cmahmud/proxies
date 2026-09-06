# SyndProxy validated proxy pool

## Current pool

- Alive now: 485
- Gold now: 390
- HTTP: 99 alive / 65 gold
- HTTPS: 29 alive / 14 gold
- SOCKS4: 171 alive / 152 gold
- SOCKS5: 186 alive / 159 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48239
- Ever gold: 1526

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
