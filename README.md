# SyndProxy validated proxy pool

## Current pool

- Alive now: 411
- Gold now: 315
- HTTP: 103 alive / 79 gold
- HTTPS: 62 alive / 23 gold
- SOCKS4: 86 alive / 76 gold
- SOCKS5: 160 alive / 137 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47937
- Ever gold: 1505

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
