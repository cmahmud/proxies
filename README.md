# SyndProxy validated proxy pool

## Current pool

- Alive now: 694
- Gold now: 455
- HTTP: 145 alive / 90 gold
- HTTPS: 149 alive / 30 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 227 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46076
- Ever gold: 1440

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
