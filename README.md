# SyndProxy validated proxy pool

## Current pool

- Alive now: 571
- Gold now: 437
- HTTP: 98 alive / 71 gold
- HTTPS: 109 alive / 28 gold
- SOCKS4: 175 alive / 163 gold
- SOCKS5: 189 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47461
- Ever gold: 1469

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
