# SyndProxy validated proxy pool

## Current pool

- Alive now: 575
- Gold now: 444
- HTTP: 100 alive / 77 gold
- HTTPS: 101 alive / 28 gold
- SOCKS4: 185 alive / 162 gold
- SOCKS5: 189 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47532
- Ever gold: 1469

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
