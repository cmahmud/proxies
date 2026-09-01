# SyndProxy validated proxy pool

## Current pool

- Alive now: 508
- Gold now: 422
- HTTP: 79 alive / 65 gold
- HTTPS: 77 alive / 26 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 180 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47145
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
