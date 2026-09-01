# SyndProxy validated proxy pool

## Current pool

- Alive now: 499
- Gold now: 419
- HTTP: 86 alive / 65 gold
- HTTPS: 67 alive / 26 gold
- SOCKS4: 165 alive / 159 gold
- SOCKS5: 181 alive / 169 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47162
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
