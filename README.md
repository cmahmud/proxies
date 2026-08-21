# SyndProxy private pool

## Current pool

- Alive now: 1005
- Gold now: 425
- HTTP: 319 alive / 91 gold
- HTTPS: 220 alive / 26 gold
- SOCKS4: 235 alive / 157 gold
- SOCKS5: 231 alive / 151 gold

## Historical pool

- Discovered: 158244
- Ever alive: 30044
- Ever gold: 1139

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
