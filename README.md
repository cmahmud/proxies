# SyndProxy validated proxy pool

## Current pool

- Alive now: 477
- Gold now: 410
- HTTP: 73 alive / 55 gold
- HTTPS: 52 alive / 22 gold
- SOCKS4: 169 alive / 163 gold
- SOCKS5: 183 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47102
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
