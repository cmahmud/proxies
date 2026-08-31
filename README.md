# SyndProxy validated proxy pool

## Current pool

- Alive now: 687
- Gold now: 467
- HTTP: 145 alive / 94 gold
- HTTPS: 127 alive / 34 gold
- SOCKS4: 179 alive / 162 gold
- SOCKS5: 236 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46210
- Ever gold: 1442

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
