# SyndProxy validated proxy pool

## Current pool

- Alive now: 654
- Gold now: 462
- HTTP: 129 alive / 90 gold
- HTTPS: 134 alive / 36 gold
- SOCKS4: 180 alive / 161 gold
- SOCKS5: 211 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46477
- Ever gold: 1444

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
