# SyndProxy validated proxy pool

## Current pool

- Alive now: 566
- Gold now: 442
- HTTP: 96 alive / 76 gold
- HTTPS: 101 alive / 30 gold
- SOCKS4: 180 alive / 161 gold
- SOCKS5: 189 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47521
- Ever gold: 1469

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
