# SyndProxy validated proxy pool

## Current pool

- Alive now: 581
- Gold now: 440
- HTTP: 98 alive / 75 gold
- HTTPS: 110 alive / 30 gold
- SOCKS4: 188 alive / 160 gold
- SOCKS5: 185 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47510
- Ever gold: 1469

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
