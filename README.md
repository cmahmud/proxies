# SyndProxy validated proxy pool

## Current pool

- Alive now: 526
- Gold now: 372
- HTTP: 135 alive / 78 gold
- HTTPS: 62 alive / 25 gold
- SOCKS4: 148 alive / 120 gold
- SOCKS5: 181 alive / 149 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47999
- Ever gold: 1509

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
