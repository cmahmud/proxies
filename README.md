# SyndProxy validated proxy pool

## Current pool

- Alive now: 693
- Gold now: 467
- HTTP: 150 alive / 96 gold
- HTTPS: 146 alive / 32 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 224 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46159
- Ever gold: 1442

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
