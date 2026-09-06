# SyndProxy validated proxy pool

## Current pool

- Alive now: 424
- Gold now: 353
- HTTP: 80 alive / 67 gold
- HTTPS: 35 alive / 16 gold
- SOCKS4: 152 alive / 141 gold
- SOCKS5: 157 alive / 129 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48379
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
