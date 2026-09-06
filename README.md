# SyndProxy validated proxy pool

## Current pool

- Alive now: 523
- Gold now: 367
- HTTP: 135 alive / 80 gold
- HTTPS: 65 alive / 24 gold
- SOCKS4: 144 alive / 117 gold
- SOCKS5: 179 alive / 146 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47999
- Ever gold: 1509

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
