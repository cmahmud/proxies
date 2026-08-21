# SyndProxy private pool

## Current pool

- Alive now: 768
- Gold now: 416
- HTTP: 199 alive / 86 gold
- HTTPS: 129 alive / 24 gold
- SOCKS4: 220 alive / 146 gold
- SOCKS5: 220 alive / 160 gold

## Historical pool

- Discovered: 151687
- Ever alive: 27727
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
