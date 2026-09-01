# SyndProxy validated proxy pool

## Current pool

- Alive now: 478
- Gold now: 411
- HTTP: 73 alive / 55 gold
- HTTPS: 56 alive / 23 gold
- SOCKS4: 168 alive / 163 gold
- SOCKS5: 181 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47101
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
