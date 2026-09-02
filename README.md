# SyndProxy validated proxy pool

## Current pool

- Alive now: 597
- Gold now: 438
- HTTP: 126 alive / 82 gold
- HTTPS: 103 alive / 24 gold
- SOCKS4: 181 alive / 160 gold
- SOCKS5: 187 alive / 172 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47655
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
