# SyndProxy validated proxy pool

## Current pool

- Alive now: 500
- Gold now: 418
- HTTP: 85 alive / 68 gold
- HTTPS: 65 alive / 25 gold
- SOCKS4: 166 alive / 158 gold
- SOCKS5: 184 alive / 167 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47165
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
