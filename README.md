# SyndProxy validated proxy pool

## Current pool

- Alive now: 693
- Gold now: 459
- HTTP: 142 alive / 93 gold
- HTTPS: 151 alive / 31 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 224 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46113
- Ever gold: 1440

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
