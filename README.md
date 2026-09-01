# SyndProxy validated proxy pool

## Current pool

- Alive now: 500
- Gold now: 423
- HTTP: 76 alive / 66 gold
- HTTPS: 75 alive / 26 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 181 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47146
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
