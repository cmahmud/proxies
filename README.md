# SyndProxy validated proxy pool

## Current pool

- Alive now: 486
- Gold now: 395
- HTTP: 94 alive / 70 gold
- HTTPS: 31 alive / 14 gold
- SOCKS4: 175 alive / 151 gold
- SOCKS5: 186 alive / 160 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48245
- Ever gold: 1526

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
