# SyndProxy validated proxy pool

## Current pool

- Alive now: 538
- Gold now: 411
- HTTP: 81 alive / 64 gold
- HTTPS: 113 alive / 23 gold
- SOCKS4: 169 alive / 158 gold
- SOCKS5: 175 alive / 166 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47227
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
