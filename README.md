# SyndProxy validated proxy pool

## Current pool

- Alive now: 462
- Gold now: 402
- HTTP: 69 alive / 49 gold
- HTTPS: 39 alive / 22 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 183 alive / 169 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47110
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
