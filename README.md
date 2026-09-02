# SyndProxy validated proxy pool

## Current pool

- Alive now: 547
- Gold now: 438
- HTTP: 87 alive / 69 gold
- HTTPS: 88 alive / 29 gold
- SOCKS4: 182 alive / 164 gold
- SOCKS5: 190 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47463
- Ever gold: 1469

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
