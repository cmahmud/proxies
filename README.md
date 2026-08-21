# SyndProxy private pool

## Current pool

- Alive now: 880
- Gold now: 405
- HTTP: 263 alive / 86 gold
- HTTPS: 175 alive / 21 gold
- SOCKS4: 197 alive / 137 gold
- SOCKS5: 245 alive / 161 gold

## Historical pool

- Discovered: 154719
- Ever alive: 29052
- Ever gold: 1121

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
