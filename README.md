# SyndProxy validated proxy pool

## Current pool

- Alive now: 423
- Gold now: 342
- HTTP: 83 alive / 65 gold
- HTTPS: 42 alive / 16 gold
- SOCKS4: 153 alive / 136 gold
- SOCKS5: 145 alive / 125 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48364
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
