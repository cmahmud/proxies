# SyndProxy validated proxy pool

## Current pool

- Alive now: 525
- Gold now: 407
- HTTP: 107 alive / 79 gold
- HTTPS: 69 alive / 20 gold
- SOCKS4: 165 alive / 150 gold
- SOCKS5: 184 alive / 158 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48059
- Ever gold: 1517

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
