# SyndProxy private pool

## Current pool

- Alive now: 937
- Gold now: 423
- HTTP: 271 alive / 86 gold
- HTTPS: 176 alive / 30 gold
- SOCKS4: 226 alive / 148 gold
- SOCKS5: 264 alive / 159 gold

## Historical pool

- Discovered: 153852
- Ever alive: 28890
- Ever gold: 1114

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
