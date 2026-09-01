# SyndProxy validated proxy pool

## Current pool

- Alive now: 608
- Gold now: 454
- HTTP: 127 alive / 85 gold
- HTTPS: 123 alive / 31 gold
- SOCKS4: 170 alive / 160 gold
- SOCKS5: 188 alive / 178 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46787
- Ever gold: 1451

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
