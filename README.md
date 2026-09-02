# SyndProxy validated proxy pool

## Current pool

- Alive now: 564
- Gold now: 440
- HTTP: 94 alive / 74 gold
- HTTPS: 102 alive / 29 gold
- SOCKS4: 181 alive / 162 gold
- SOCKS5: 187 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47520
- Ever gold: 1469

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
