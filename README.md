# SyndProxy validated proxy pool

## Current pool

- Alive now: 666
- Gold now: 460
- HTTP: 137 alive / 94 gold
- HTTPS: 137 alive / 30 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 220 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46121
- Ever gold: 1440

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
