# SyndProxy validated proxy pool

## Current pool

- Alive now: 418
- Gold now: 341
- HTTP: 83 alive / 64 gold
- HTTPS: 41 alive / 16 gold
- SOCKS4: 150 alive / 136 gold
- SOCKS5: 144 alive / 125 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48364
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
