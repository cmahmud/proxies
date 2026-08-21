# SyndProxy private pool

## Current pool

- Alive now: 879
- Gold now: 413
- HTTP: 266 alive / 90 gold
- HTTPS: 183 alive / 24 gold
- SOCKS4: 193 alive / 138 gold
- SOCKS5: 237 alive / 161 gold

## Historical pool

- Discovered: 154719
- Ever alive: 29057
- Ever gold: 1122

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
