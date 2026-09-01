# SyndProxy validated proxy pool

## Current pool

- Alive now: 651
- Gold now: 474
- HTTP: 145 alive / 96 gold
- HTTPS: 137 alive / 40 gold
- SOCKS4: 174 alive / 163 gold
- SOCKS5: 195 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46941
- Ever gold: 1457

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
