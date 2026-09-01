# SyndProxy validated proxy pool

## Current pool

- Alive now: 652
- Gold now: 456
- HTTP: 116 alive / 91 gold
- HTTPS: 129 alive / 29 gold
- SOCKS4: 183 alive / 162 gold
- SOCKS5: 224 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46554
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
