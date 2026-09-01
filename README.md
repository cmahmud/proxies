# SyndProxy validated proxy pool

## Current pool

- Alive now: 556
- Gold now: 447
- HTTP: 105 alive / 80 gold
- HTTPS: 91 alive / 30 gold
- SOCKS4: 171 alive / 160 gold
- SOCKS5: 189 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47380
- Ever gold: 1467

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
