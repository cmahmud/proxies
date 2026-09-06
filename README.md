# SyndProxy validated proxy pool

## Current pool

- Alive now: 407
- Gold now: 315
- HTTP: 78 alive / 58 gold
- HTTPS: 28 alive / 10 gold
- SOCKS4: 146 alive / 129 gold
- SOCKS5: 155 alive / 118 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48382
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
