# SyndProxy validated proxy pool

## Current pool

- Alive now: 523
- Gold now: 368
- HTTP: 135 alive / 79 gold
- HTTPS: 64 alive / 25 gold
- SOCKS4: 146 alive / 118 gold
- SOCKS5: 178 alive / 146 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47999
- Ever gold: 1509

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
