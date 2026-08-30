# SyndProxy validated proxy pool

## Current pool

- Alive now: 617
- Gold now: 474
- HTTP: 136 alive / 96 gold
- HTTPS: 118 alive / 42 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 193 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44872
- Ever gold: 1417

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
