# SyndProxy validated proxy pool

## Current pool

- Alive now: 577
- Gold now: 444
- HTTP: 87 alive / 71 gold
- HTTPS: 126 alive / 33 gold
- SOCKS4: 177 alive / 164 gold
- SOCKS5: 187 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47484
- Ever gold: 1469

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
