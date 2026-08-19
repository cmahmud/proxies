# SyndProxy private pool

## Current pool

- Alive now: 1090
- Gold now: 399
- HTTP: 323 alive / 73 gold
- HTTPS: 245 alive / 12 gold
- SOCKS4: 255 alive / 153 gold
- SOCKS5: 267 alive / 161 gold

## Historical pool

- Discovered: 131115
- Ever alive: 20612
- Ever gold: 869

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
