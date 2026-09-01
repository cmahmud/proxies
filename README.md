# SyndProxy validated proxy pool

## Current pool

- Alive now: 554
- Gold now: 435
- HTTP: 98 alive / 72 gold
- HTTPS: 99 alive / 29 gold
- SOCKS4: 168 alive / 158 gold
- SOCKS5: 189 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47334
- Ever gold: 1466

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
