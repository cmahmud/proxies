# SyndProxy validated proxy pool

## Current pool

- Alive now: 417
- Gold now: 340
- HTTP: 85 alive / 60 gold
- HTTPS: 29 alive / 12 gold
- SOCKS4: 142 alive / 135 gold
- SOCKS5: 161 alive / 133 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48384
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
