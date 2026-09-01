# SyndProxy validated proxy pool

## Current pool

- Alive now: 654
- Gold now: 456
- HTTP: 117 alive / 91 gold
- HTTPS: 129 alive / 29 gold
- SOCKS4: 184 alive / 162 gold
- SOCKS5: 224 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46555
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
