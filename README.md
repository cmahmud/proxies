# SyndProxy private pool

## Current pool

- Alive now: 1019
- Gold now: 424
- HTTP: 305 alive / 87 gold
- HTTPS: 211 alive / 21 gold
- SOCKS4: 235 alive / 162 gold
- SOCKS5: 268 alive / 154 gold

## Historical pool

- Discovered: 158238
- Ever alive: 30010
- Ever gold: 1139

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
