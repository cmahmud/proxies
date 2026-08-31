# SyndProxy validated proxy pool

## Current pool

- Alive now: 694
- Gold now: 464
- HTTP: 151 alive / 94 gold
- HTTPS: 130 alive / 33 gold
- SOCKS4: 182 alive / 161 gold
- SOCKS5: 231 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46228
- Ever gold: 1442

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
