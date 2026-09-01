# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 412
- HTTP: 82 alive / 66 gold
- HTTPS: 104 alive / 24 gold
- SOCKS4: 169 alive / 157 gold
- SOCKS5: 174 alive / 165 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47231
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
