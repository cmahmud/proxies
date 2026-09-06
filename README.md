# SyndProxy validated proxy pool

## Current pool

- Alive now: 481
- Gold now: 394
- HTTP: 90 alive / 61 gold
- HTTPS: 36 alive / 13 gold
- SOCKS4: 170 alive / 158 gold
- SOCKS5: 185 alive / 162 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48253
- Ever gold: 1526

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
