# SyndProxy validated proxy pool

## Current pool

- Alive now: 424
- Gold now: 317
- HTTP: 106 alive / 78 gold
- HTTPS: 63 alive / 21 gold
- SOCKS4: 91 alive / 79 gold
- SOCKS5: 164 alive / 139 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47943
- Ever gold: 1505

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
