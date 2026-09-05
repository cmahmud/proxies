# SyndProxy validated proxy pool

## Current pool

- Alive now: 383
- Gold now: 300
- HTTP: 106 alive / 80 gold
- HTTPS: 52 alive / 22 gold
- SOCKS4: 71 alive / 65 gold
- SOCKS5: 154 alive / 133 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47921
- Ever gold: 1504

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
