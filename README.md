# SyndProxy validated proxy pool

## Current pool

- Alive now: 482
- Gold now: 409
- HTTP: 87 alive / 59 gold
- HTTPS: 44 alive / 21 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 179 alive / 168 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47081
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
