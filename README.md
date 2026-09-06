# SyndProxy validated proxy pool

## Current pool

- Alive now: 497
- Gold now: 401
- HTTP: 95 alive / 61 gold
- HTTPS: 38 alive / 17 gold
- SOCKS4: 175 alive / 158 gold
- SOCKS5: 189 alive / 165 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48253
- Ever gold: 1526

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
