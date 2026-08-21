# SyndProxy private pool

## Current pool

- Alive now: 901
- Gold now: 365
- HTTP: 296 alive / 92 gold
- HTTPS: 189 alive / 24 gold
- SOCKS4: 192 alive / 138 gold
- SOCKS5: 224 alive / 111 gold

## Historical pool

- Discovered: 154713
- Ever alive: 28997
- Ever gold: 1119

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
