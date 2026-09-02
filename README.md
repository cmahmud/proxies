# SyndProxy validated proxy pool

## Current pool

- Alive now: 556
- Gold now: 441
- HTTP: 97 alive / 72 gold
- HTTPS: 99 alive / 29 gold
- SOCKS4: 173 alive / 163 gold
- SOCKS5: 187 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47460
- Ever gold: 1469

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
