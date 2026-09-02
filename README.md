# SyndProxy validated proxy pool

## Current pool

- Alive now: 570
- Gold now: 442
- HTTP: 95 alive / 76 gold
- HTTPS: 108 alive / 30 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 190 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47524
- Ever gold: 1469

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
