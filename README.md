# SyndProxy validated proxy pool

## Current pool

- Alive now: 619
- Gold now: 460
- HTTP: 127 alive / 89 gold
- HTTPS: 126 alive / 33 gold
- SOCKS4: 171 alive / 160 gold
- SOCKS5: 195 alive / 178 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46772
- Ever gold: 1451

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
