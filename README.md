# SyndProxy validated proxy pool

## Current pool

- Alive now: 648
- Gold now: 485
- HTTP: 144 alive / 102 gold
- HTTPS: 123 alive / 44 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 204 alive / 177 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44933
- Ever gold: 1419

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
