# SyndProxy validated proxy pool

## Current pool

- Alive now: 695
- Gold now: 465
- HTTP: 152 alive / 96 gold
- HTTPS: 129 alive / 32 gold
- SOCKS4: 183 alive / 162 gold
- SOCKS5: 231 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46232
- Ever gold: 1442

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
