# SyndProxy validated proxy pool

## Current pool

- Alive now: 570
- Gold now: 442
- HTTP: 96 alive / 78 gold
- HTTPS: 111 alive / 29 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 187 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47528
- Ever gold: 1469

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
