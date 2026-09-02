# SyndProxy validated proxy pool

## Current pool

- Alive now: 565
- Gold now: 444
- HTTP: 94 alive / 78 gold
- HTTPS: 107 alive / 30 gold
- SOCKS4: 179 alive / 162 gold
- SOCKS5: 185 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47526
- Ever gold: 1469

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
