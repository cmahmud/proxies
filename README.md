# SyndProxy validated proxy pool

## Current pool

- Alive now: 671
- Gold now: 467
- HTTP: 142 alive / 95 gold
- HTTPS: 119 alive / 34 gold
- SOCKS4: 178 alive / 162 gold
- SOCKS5: 232 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46195
- Ever gold: 1442

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
