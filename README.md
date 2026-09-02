# SyndProxy validated proxy pool

## Current pool

- Alive now: 566
- Gold now: 442
- HTTP: 97 alive / 79 gold
- HTTPS: 110 alive / 28 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 185 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47528
- Ever gold: 1469

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
