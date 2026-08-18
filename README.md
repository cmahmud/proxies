# SyndProxy private pool

## Current pool

- Alive now: 640
- Gold now: 211
- HTTP: 189 alive / 26 gold
- HTTPS: 89 alive / 9 gold
- SOCKS4: 174 alive / 96 gold
- SOCKS5: 188 alive / 80 gold

## Historical pool

- Discovered: 86775
- Ever alive: 7650
- Ever gold: 343

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
