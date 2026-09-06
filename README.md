# SyndProxy validated proxy pool

## Current pool

- Alive now: 479
- Gold now: 396
- HTTP: 91 alive / 62 gold
- HTTPS: 35 alive / 13 gold
- SOCKS4: 168 alive / 157 gold
- SOCKS5: 185 alive / 164 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48253
- Ever gold: 1526

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
