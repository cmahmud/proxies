# SyndProxy validated proxy pool

## Current pool

- Alive now: 685
- Gold now: 457
- HTTP: 140 alive / 91 gold
- HTTPS: 147 alive / 30 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 227 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46069
- Ever gold: 1440

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
