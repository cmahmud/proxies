# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 405
- HTTP: 83 alive / 63 gold
- HTTPS: 104 alive / 23 gold
- SOCKS4: 166 alive / 158 gold
- SOCKS5: 175 alive / 161 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47212
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
