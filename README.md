# SyndProxy validated proxy pool

## Current pool

- Alive now: 563
- Gold now: 444
- HTTP: 96 alive / 79 gold
- HTTPS: 103 alive / 30 gold
- SOCKS4: 178 alive / 161 gold
- SOCKS5: 186 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47526
- Ever gold: 1469

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
