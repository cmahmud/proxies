# SyndProxy validated proxy pool

## Current pool

- Alive now: 625
- Gold now: 461
- HTTP: 134 alive / 87 gold
- HTTPS: 126 alive / 34 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 195 alive / 179 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46769
- Ever gold: 1451

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
