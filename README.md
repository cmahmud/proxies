# SyndProxy validated proxy pool

## Current pool

- Alive now: 544
- Gold now: 423
- HTTP: 87 alive / 68 gold
- HTTPS: 106 alive / 27 gold
- SOCKS4: 175 alive / 158 gold
- SOCKS5: 176 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47274
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
