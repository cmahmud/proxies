# SyndProxy validated proxy pool

## Current pool

- Alive now: 504
- Gold now: 417
- HTTP: 84 alive / 67 gold
- HTTPS: 73 alive / 25 gold
- SOCKS4: 166 alive / 158 gold
- SOCKS5: 181 alive / 167 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47165
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
