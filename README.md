# SyndProxy validated proxy pool

## Current pool

- Alive now: 638
- Gold now: 477
- HTTP: 136 alive / 99 gold
- HTTPS: 129 alive / 42 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 199 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45095
- Ever gold: 1423

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
