# SyndProxy validated proxy pool

## Current pool

- Alive now: 550
- Gold now: 432
- HTTP: 93 alive / 72 gold
- HTTPS: 106 alive / 31 gold
- SOCKS4: 171 alive / 158 gold
- SOCKS5: 180 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47300
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
