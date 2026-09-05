# SyndProxy validated proxy pool

## Current pool

- Alive now: 406
- Gold now: 319
- HTTP: 104 alive / 80 gold
- HTTPS: 57 alive / 24 gold
- SOCKS4: 87 alive / 76 gold
- SOCKS5: 158 alive / 139 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47935
- Ever gold: 1505

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
