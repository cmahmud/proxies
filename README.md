# SyndProxy validated proxy pool

## Current pool

- Alive now: 577
- Gold now: 439
- HTTP: 92 alive / 73 gold
- HTTPS: 110 alive / 30 gold
- SOCKS4: 187 alive / 162 gold
- SOCKS5: 188 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47513
- Ever gold: 1469

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
