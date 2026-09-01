# SyndProxy validated proxy pool

## Current pool

- Alive now: 612
- Gold now: 462
- HTTP: 134 alive / 89 gold
- HTTPS: 121 alive / 37 gold
- SOCKS4: 170 alive / 164 gold
- SOCKS5: 187 alive / 172 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46903
- Ever gold: 1456

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
