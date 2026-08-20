# SyndProxy private pool

## Current pool

- Alive now: 699
- Gold now: 396
- HTTP: 161 alive / 82 gold
- HTTPS: 127 alive / 22 gold
- SOCKS4: 183 alive / 127 gold
- SOCKS5: 228 alive / 165 gold

## Historical pool

- Discovered: 151041
- Ever alive: 27119
- Ever gold: 1092

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
