# SyndProxy validated proxy pool

## Current pool

- Alive now: 424
- Gold now: 343
- HTTP: 87 alive / 64 gold
- HTTPS: 31 alive / 14 gold
- SOCKS4: 149 alive / 134 gold
- SOCKS5: 157 alive / 131 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48382
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
