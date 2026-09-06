# SyndProxy validated proxy pool

## Current pool

- Alive now: 504
- Gold now: 396
- HTTP: 108 alive / 73 gold
- HTTPS: 44 alive / 15 gold
- SOCKS4: 168 alive / 153 gold
- SOCKS5: 184 alive / 155 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48102
- Ever gold: 1519

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
