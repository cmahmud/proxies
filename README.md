# SyndProxy private pool

## Current pool

- Alive now: 1022
- Gold now: 424
- HTTP: 308 alive / 88 gold
- HTTPS: 213 alive / 20 gold
- SOCKS4: 236 alive / 162 gold
- SOCKS5: 265 alive / 154 gold

## Historical pool

- Discovered: 158238
- Ever alive: 30009
- Ever gold: 1139

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
