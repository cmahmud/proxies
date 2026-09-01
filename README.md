# SyndProxy validated proxy pool

## Current pool

- Alive now: 562
- Gold now: 448
- HTTP: 103 alive / 80 gold
- HTTPS: 101 alive / 30 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 187 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47384
- Ever gold: 1467

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
