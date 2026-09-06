# SyndProxy validated proxy pool

## Current pool

- Alive now: 417
- Gold now: 337
- HTTP: 84 alive / 62 gold
- HTTPS: 30 alive / 10 gold
- SOCKS4: 144 alive / 135 gold
- SOCKS5: 159 alive / 130 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48383
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
