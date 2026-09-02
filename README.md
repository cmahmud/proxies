# SyndProxy validated proxy pool

## Current pool

- Alive now: 570
- Gold now: 439
- HTTP: 93 alive / 70 gold
- HTTPS: 111 alive / 30 gold
- SOCKS4: 177 alive / 163 gold
- SOCKS5: 189 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47462
- Ever gold: 1469

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
