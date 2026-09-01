# SyndProxy validated proxy pool

## Current pool

- Alive now: 616
- Gold now: 472
- HTTP: 129 alive / 91 gold
- HTTPS: 117 alive / 44 gold
- SOCKS4: 175 alive / 163 gold
- SOCKS5: 195 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46960
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
