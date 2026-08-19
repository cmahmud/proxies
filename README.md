# SyndProxy private pool

## Current pool

- Alive now: 836
- Gold now: 321
- HTTP: 267 alive / 53 gold
- HTTPS: 171 alive / 11 gold
- SOCKS4: 206 alive / 131 gold
- SOCKS5: 192 alive / 126 gold

## Historical pool

- Discovered: 127417
- Ever alive: 20003
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
