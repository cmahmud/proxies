# SyndProxy validated proxy pool

## Current pool

- Alive now: 486
- Gold now: 404
- HTTP: 96 alive / 72 gold
- HTTPS: 34 alive / 14 gold
- SOCKS4: 170 alive / 153 gold
- SOCKS5: 186 alive / 165 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48246
- Ever gold: 1526

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
