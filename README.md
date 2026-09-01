# SyndProxy validated proxy pool

## Current pool

- Alive now: 537
- Gold now: 422
- HTTP: 93 alive / 68 gold
- HTTPS: 97 alive / 29 gold
- SOCKS4: 169 alive / 157 gold
- SOCKS5: 178 alive / 168 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47265
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
