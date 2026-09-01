# SyndProxy validated proxy pool

## Current pool

- Alive now: 503
- Gold now: 426
- HTTP: 78 alive / 70 gold
- HTTPS: 75 alive / 25 gold
- SOCKS4: 174 alive / 160 gold
- SOCKS5: 176 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47149
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
