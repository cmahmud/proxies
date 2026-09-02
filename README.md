# SyndProxy validated proxy pool

## Current pool

- Alive now: 550
- Gold now: 437
- HTTP: 92 alive / 70 gold
- HTTPS: 97 alive / 28 gold
- SOCKS4: 173 alive / 163 gold
- SOCKS5: 188 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47460
- Ever gold: 1469

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
