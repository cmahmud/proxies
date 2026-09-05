# SyndProxy validated proxy pool

## Current pool

- Alive now: 386
- Gold now: 308
- HTTP: 102 alive / 78 gold
- HTTPS: 48 alive / 22 gold
- SOCKS4: 82 alive / 73 gold
- SOCKS5: 154 alive / 135 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47928
- Ever gold: 1505

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
