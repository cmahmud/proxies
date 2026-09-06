# SyndProxy validated proxy pool

## Current pool

- Alive now: 554
- Gold now: 386
- HTTP: 153 alive / 81 gold
- HTTPS: 62 alive / 24 gold
- SOCKS4: 157 alive / 131 gold
- SOCKS5: 182 alive / 150 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48014
- Ever gold: 1510

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
