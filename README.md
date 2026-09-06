# SyndProxy validated proxy pool

## Current pool

- Alive now: 407
- Gold now: 309
- HTTP: 82 alive / 55 gold
- HTTPS: 32 alive / 6 gold
- SOCKS4: 146 alive / 133 gold
- SOCKS5: 147 alive / 115 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48372
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
