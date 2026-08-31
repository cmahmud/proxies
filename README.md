# SyndProxy validated proxy pool

## Current pool

- Alive now: 626
- Gold now: 477
- HTTP: 136 alive / 99 gold
- HTTPS: 126 alive / 42 gold
- SOCKS4: 169 alive / 162 gold
- SOCKS5: 195 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45040
- Ever gold: 1422

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
