# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 374
- HTTP: 132 alive / 80 gold
- HTTPS: 56 alive / 23 gold
- SOCKS4: 151 alive / 122 gold
- SOCKS5: 181 alive / 149 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48002
- Ever gold: 1509

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
