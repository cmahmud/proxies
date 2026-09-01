# SyndProxy validated proxy pool

## Current pool

- Alive now: 625
- Gold now: 465
- HTTP: 132 alive / 92 gold
- HTTPS: 108 alive / 35 gold
- SOCKS4: 180 alive / 162 gold
- SOCKS5: 205 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46400
- Ever gold: 1444

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
