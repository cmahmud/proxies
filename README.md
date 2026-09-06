# SyndProxy validated proxy pool

## Current pool

- Alive now: 523
- Gold now: 375
- HTTP: 133 alive / 80 gold
- HTTPS: 58 alive / 23 gold
- SOCKS4: 150 alive / 122 gold
- SOCKS5: 182 alive / 150 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48005
- Ever gold: 1509

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
