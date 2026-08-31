# SyndProxy validated proxy pool

## Current pool

- Alive now: 733
- Gold now: 460
- HTTP: 158 alive / 94 gold
- HTTPS: 138 alive / 30 gold
- SOCKS4: 184 alive / 162 gold
- SOCKS5: 253 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46272
- Ever gold: 1442

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
