# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 423
- HTTP: 90 alive / 68 gold
- HTTPS: 71 alive / 26 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 183 alive / 167 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47071
- Ever gold: 1464

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
