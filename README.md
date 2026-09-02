# SyndProxy validated proxy pool

## Current pool

- Alive now: 567
- Gold now: 443
- HTTP: 93 alive / 71 gold
- HTTPS: 103 alive / 31 gold
- SOCKS4: 180 alive / 163 gold
- SOCKS5: 191 alive / 178 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47474
- Ever gold: 1469

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
