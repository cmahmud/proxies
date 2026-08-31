# SyndProxy validated proxy pool

## Current pool

- Alive now: 684
- Gold now: 467
- HTTP: 143 alive / 96 gold
- HTTPS: 145 alive / 33 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 224 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46159
- Ever gold: 1442

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
