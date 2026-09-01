# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 419
- HTTP: 84 alive / 67 gold
- HTTPS: 85 alive / 24 gold
- SOCKS4: 177 alive / 160 gold
- SOCKS5: 184 alive / 168 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47139
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
