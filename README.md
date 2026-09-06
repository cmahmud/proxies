# SyndProxy validated proxy pool

## Current pool

- Alive now: 532
- Gold now: 374
- HTTP: 138 alive / 79 gold
- HTTPS: 60 alive / 23 gold
- SOCKS4: 152 alive / 122 gold
- SOCKS5: 182 alive / 150 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48001
- Ever gold: 1509

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
