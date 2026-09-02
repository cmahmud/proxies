# SyndProxy validated proxy pool

## Current pool

- Alive now: 557
- Gold now: 437
- HTTP: 89 alive / 70 gold
- HTTPS: 106 alive / 30 gold
- SOCKS4: 174 alive / 164 gold
- SOCKS5: 188 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47490
- Ever gold: 1469

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
