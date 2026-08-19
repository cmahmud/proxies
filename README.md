# SyndProxy private pool

## Current pool

- Alive now: 791
- Gold now: 307
- HTTP: 222 alive / 57 gold
- HTTPS: 161 alive / 11 gold
- SOCKS4: 213 alive / 116 gold
- SOCKS5: 195 alive / 123 gold

## Historical pool

- Discovered: 129265
- Ever alive: 20145
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
