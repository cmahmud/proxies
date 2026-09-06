# SyndProxy validated proxy pool

## Current pool

- Alive now: 392
- Gold now: 303
- HTTP: 74 alive / 47 gold
- HTTPS: 28 alive / 8 gold
- SOCKS4: 149 alive / 133 gold
- SOCKS5: 141 alive / 115 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48329
- Ever gold: 1529

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
