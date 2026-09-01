# SyndProxy validated proxy pool

## Current pool

- Alive now: 490
- Gold now: 419
- HTTP: 83 alive / 62 gold
- HTTPS: 55 alive / 25 gold
- SOCKS4: 172 alive / 164 gold
- SOCKS5: 180 alive / 168 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47074
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
