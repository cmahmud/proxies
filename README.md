# SyndProxy validated proxy pool

## Current pool

- Alive now: 420
- Gold now: 332
- HTTP: 80 alive / 60 gold
- HTTPS: 32 alive / 9 gold
- SOCKS4: 149 alive / 137 gold
- SOCKS5: 159 alive / 126 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48381
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
