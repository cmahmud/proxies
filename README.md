# SyndProxy validated proxy pool

## Current pool

- Alive now: 655
- Gold now: 456
- HTTP: 124 alive / 88 gold
- HTTPS: 127 alive / 32 gold
- SOCKS4: 178 alive / 162 gold
- SOCKS5: 226 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46543
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
