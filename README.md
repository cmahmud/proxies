# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 398
- HTTP: 98 alive / 61 gold
- HTTPS: 38 alive / 17 gold
- SOCKS4: 176 alive / 158 gold
- SOCKS5: 190 alive / 162 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48253
- Ever gold: 1526

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
