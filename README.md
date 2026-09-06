# SyndProxy validated proxy pool

## Current pool

- Alive now: 402
- Gold now: 313
- HTTP: 82 alive / 49 gold
- HTTPS: 31 alive / 8 gold
- SOCKS4: 147 alive / 134 gold
- SOCKS5: 142 alive / 122 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48329
- Ever gold: 1529

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
