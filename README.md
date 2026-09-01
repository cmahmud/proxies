# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 414
- HTTP: 83 alive / 65 gold
- HTTPS: 100 alive / 22 gold
- SOCKS4: 167 alive / 159 gold
- SOCKS5: 183 alive / 168 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47180
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
