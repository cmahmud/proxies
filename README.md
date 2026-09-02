# SyndProxy validated proxy pool

## Current pool

- Alive now: 581
- Gold now: 442
- HTTP: 99 alive / 75 gold
- HTTPS: 111 alive / 30 gold
- SOCKS4: 186 alive / 162 gold
- SOCKS5: 185 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47512
- Ever gold: 1469

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
