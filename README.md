# SyndProxy validated proxy pool

## Current pool

- Alive now: 566
- Gold now: 434
- HTTP: 98 alive / 71 gold
- HTTPS: 105 alive / 30 gold
- SOCKS4: 176 alive / 159 gold
- SOCKS5: 187 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47328
- Ever gold: 1466

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
