# SyndProxy validated proxy pool

## Current pool

- Alive now: 460
- Gold now: 401
- HTTP: 68 alive / 48 gold
- HTTPS: 38 alive / 22 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 183 alive / 169 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47110
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
