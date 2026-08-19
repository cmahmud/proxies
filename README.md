# SyndProxy private pool

## Current pool

- Alive now: 820
- Gold now: 323
- HTTP: 256 alive / 55 gold
- HTTPS: 170 alive / 11 gold
- SOCKS4: 203 alive / 131 gold
- SOCKS5: 191 alive / 126 gold

## Historical pool

- Discovered: 127417
- Ever alive: 20000
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
