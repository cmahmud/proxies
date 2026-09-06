# SyndProxy validated proxy pool

## Current pool

- Alive now: 420
- Gold now: 321
- HTTP: 85 alive / 57 gold
- HTTPS: 40 alive / 11 gold
- SOCKS4: 149 alive / 134 gold
- SOCKS5: 146 alive / 119 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48359
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
