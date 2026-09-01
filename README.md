# SyndProxy validated proxy pool

## Current pool

- Alive now: 629
- Gold now: 460
- HTTP: 143 alive / 93 gold
- HTTPS: 114 alive / 34 gold
- SOCKS4: 178 alive / 161 gold
- SOCKS5: 194 alive / 172 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46874
- Ever gold: 1453

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
