# SyndProxy validated proxy pool

## Current pool

- Alive now: 657
- Gold now: 458
- HTTP: 130 alive / 89 gold
- HTTPS: 122 alive / 33 gold
- SOCKS4: 178 alive / 162 gold
- SOCKS5: 227 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46532
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
