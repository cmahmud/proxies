# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 419
- HTTP: 83 alive / 68 gold
- HTTPS: 80 alive / 24 gold
- SOCKS4: 170 alive / 159 gold
- SOCKS5: 181 alive / 168 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47170
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
