# SyndProxy validated proxy pool

## Current pool

- Alive now: 419
- Gold now: 325
- HTTP: 87 alive / 59 gold
- HTTPS: 40 alive / 11 gold
- SOCKS4: 146 alive / 133 gold
- SOCKS5: 146 alive / 122 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48359
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
