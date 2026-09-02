# SyndProxy validated proxy pool

## Current pool

- Alive now: 558
- Gold now: 445
- HTTP: 87 alive / 72 gold
- HTTPS: 100 alive / 30 gold
- SOCKS4: 177 alive / 163 gold
- SOCKS5: 194 alive / 180 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47470
- Ever gold: 1469

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
