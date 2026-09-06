# SyndProxy validated proxy pool

## Current pool

- Alive now: 501
- Gold now: 396
- HTTP: 96 alive / 60 gold
- HTTPS: 38 alive / 16 gold
- SOCKS4: 175 alive / 158 gold
- SOCKS5: 192 alive / 162 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48253
- Ever gold: 1526

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
