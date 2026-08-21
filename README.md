# SyndProxy private pool

## Current pool

- Alive now: 863
- Gold now: 366
- HTTP: 300 alive / 103 gold
- HTTPS: 152 alive / 25 gold
- SOCKS4: 197 alive / 133 gold
- SOCKS5: 214 alive / 105 gold

## Historical pool

- Discovered: 154710
- Ever alive: 28961
- Ever gold: 1117

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
