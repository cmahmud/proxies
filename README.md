# SyndProxy validated proxy pool

## Current pool

- Alive now: 614
- Gold now: 466
- HTTP: 127 alive / 91 gold
- HTTPS: 114 alive / 36 gold
- SOCKS4: 181 alive / 162 gold
- SOCKS5: 192 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46350
- Ever gold: 1443

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
