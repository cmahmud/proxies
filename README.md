# SyndProxy validated proxy pool

## Current pool

- Alive now: 596
- Gold now: 454
- HTTP: 119 alive / 87 gold
- HTTPS: 121 alive / 30 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 189 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46736
- Ever gold: 1448

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
