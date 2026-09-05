# SyndProxy validated proxy pool

## Current pool

- Alive now: 427
- Gold now: 322
- HTTP: 105 alive / 76 gold
- HTTPS: 58 alive / 23 gold
- SOCKS4: 99 alive / 84 gold
- SOCKS5: 165 alive / 139 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47949
- Ever gold: 1505

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
