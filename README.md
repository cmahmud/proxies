# SyndProxy validated proxy pool

## Current pool

- Alive now: 657
- Gold now: 461
- HTTP: 131 alive / 90 gold
- HTTPS: 125 alive / 34 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 227 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46526
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
