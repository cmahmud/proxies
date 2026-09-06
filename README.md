# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 380
- HTTP: 141 alive / 83 gold
- HTTPS: 55 alive / 23 gold
- SOCKS4: 154 alive / 125 gold
- SOCKS5: 180 alive / 149 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48007
- Ever gold: 1509

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
