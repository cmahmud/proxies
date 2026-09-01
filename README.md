# SyndProxy validated proxy pool

## Current pool

- Alive now: 540
- Gold now: 421
- HTTP: 81 alive / 66 gold
- HTTPS: 102 alive / 25 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 183 alive / 169 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47172
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
