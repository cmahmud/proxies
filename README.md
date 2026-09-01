# SyndProxy validated proxy pool

## Current pool

- Alive now: 641
- Gold now: 461
- HTTP: 148 alive / 93 gold
- HTTPS: 125 alive / 35 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 192 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46869
- Ever gold: 1452

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
