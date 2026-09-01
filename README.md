# SyndProxy validated proxy pool

## Current pool

- Alive now: 619
- Gold now: 472
- HTTP: 131 alive / 91 gold
- HTTPS: 120 alive / 44 gold
- SOCKS4: 174 alive / 163 gold
- SOCKS5: 194 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46960
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
