# SyndProxy validated proxy pool

## Current pool

- Alive now: 547
- Gold now: 419
- HTTP: 90 alive / 66 gold
- HTTPS: 111 alive / 28 gold
- SOCKS4: 172 alive / 157 gold
- SOCKS5: 174 alive / 168 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47269
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
