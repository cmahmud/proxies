# SyndProxy validated proxy pool

## Current pool

- Alive now: 636
- Gold now: 462
- HTTP: 130 alive / 94 gold
- HTTPS: 122 alive / 34 gold
- SOCKS4: 178 alive / 160 gold
- SOCKS5: 206 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46388
- Ever gold: 1444

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
