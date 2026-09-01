# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 407
- HTTP: 82 alive / 62 gold
- HTTPS: 94 alive / 22 gold
- SOCKS4: 163 alive / 158 gold
- SOCKS5: 175 alive / 165 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47212
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
