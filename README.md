# SyndProxy validated proxy pool

## Current pool

- Alive now: 461
- Gold now: 364
- HTTP: 74 alive / 40 gold
- HTTPS: 34 alive / 9 gold
- SOCKS4: 174 alive / 154 gold
- SOCKS5: 179 alive / 161 gold

## Historical pool

- Discovered: 172855
- Ever alive: 32984
- Ever gold: 1221

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
