# SyndProxy validated proxy pool

## Current pool

- Alive now: 539
- Gold now: 419
- HTTP: 85 alive / 65 gold
- HTTPS: 97 alive / 25 gold
- SOCKS4: 175 alive / 160 gold
- SOCKS5: 182 alive / 169 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47173
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
