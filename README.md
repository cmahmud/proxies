# SyndProxy validated proxy pool

## Current pool

- Alive now: 564
- Gold now: 442
- HTTP: 90 alive / 71 gold
- HTTPS: 106 alive / 31 gold
- SOCKS4: 181 alive / 165 gold
- SOCKS5: 187 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47496
- Ever gold: 1469

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
