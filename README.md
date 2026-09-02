# SyndProxy validated proxy pool

## Current pool

- Alive now: 572
- Gold now: 444
- HTTP: 91 alive / 72 gold
- HTTPS: 107 alive / 30 gold
- SOCKS4: 181 alive / 162 gold
- SOCKS5: 193 alive / 180 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47470
- Ever gold: 1469

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
