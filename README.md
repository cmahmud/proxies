# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 417
- HTTP: 90 alive / 66 gold
- HTTPS: 93 alive / 25 gold
- SOCKS4: 168 alive / 157 gold
- SOCKS5: 179 alive / 169 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47248
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
