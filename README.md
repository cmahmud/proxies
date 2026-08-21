# SyndProxy private pool

## Current pool

- Alive now: 793
- Gold now: 413
- HTTP: 215 alive / 93 gold
- HTTPS: 170 alive / 21 gold
- SOCKS4: 190 alive / 147 gold
- SOCKS5: 218 alive / 152 gold

## Historical pool

- Discovered: 152161
- Ever alive: 27850
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
