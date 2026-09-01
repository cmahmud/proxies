# SyndProxy validated proxy pool

## Current pool

- Alive now: 556
- Gold now: 445
- HTTP: 107 alive / 79 gold
- HTTPS: 92 alive / 32 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 185 alive / 172 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47009
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
