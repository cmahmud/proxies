# SyndProxy private pool

## Current pool

- Alive now: 834
- Gold now: 366
- HTTP: 256 alive / 93 gold
- HTTPS: 173 alive / 19 gold
- SOCKS4: 198 alive / 144 gold
- SOCKS5: 207 alive / 110 gold

## Historical pool

- Discovered: 154658
- Ever alive: 28944
- Ever gold: 1116

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
