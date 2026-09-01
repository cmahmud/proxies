# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 419
- HTTP: 80 alive / 64 gold
- HTTPS: 94 alive / 25 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 188 alive / 169 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47172
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
