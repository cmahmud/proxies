# SyndProxy private pool

## Current pool

- Alive now: 1048
- Gold now: 365
- HTTP: 372 alive / 94 gold
- HTTPS: 264 alive / 21 gold
- SOCKS4: 186 alive / 116 gold
- SOCKS5: 226 alive / 134 gold

## Historical pool

- Discovered: 153747
- Ever alive: 28817
- Ever gold: 1114

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
