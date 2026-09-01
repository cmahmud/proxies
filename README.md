# SyndProxy validated proxy pool

## Current pool

- Alive now: 482
- Gold now: 419
- HTTP: 84 alive / 64 gold
- HTTPS: 50 alive / 23 gold
- SOCKS4: 169 alive / 164 gold
- SOCKS5: 179 alive / 168 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47074
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
