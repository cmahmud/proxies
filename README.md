# SyndProxy validated proxy pool

## Current pool

- Alive now: 654
- Gold now: 467
- HTTP: 127 alive / 94 gold
- HTTPS: 134 alive / 36 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 218 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46465
- Ever gold: 1444

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
