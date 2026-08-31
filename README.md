# SyndProxy validated proxy pool

## Current pool

- Alive now: 639
- Gold now: 467
- HTTP: 130 alive / 96 gold
- HTTPS: 126 alive / 33 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 210 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46018
- Ever gold: 1439

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
