# SyndProxy validated proxy pool

## Current pool

- Alive now: 483
- Gold now: 388
- HTTP: 98 alive / 70 gold
- HTTPS: 35 alive / 12 gold
- SOCKS4: 168 alive / 152 gold
- SOCKS5: 182 alive / 154 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48218
- Ever gold: 1525

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
