# SyndProxy private pool

## Current pool

- Alive now: 888
- Gold now: 402
- HTTP: 258 alive / 94 gold
- HTTPS: 199 alive / 26 gold
- SOCKS4: 224 alive / 157 gold
- SOCKS5: 207 alive / 125 gold

## Historical pool

- Discovered: 160980
- Ever alive: 30846
- Ever gold: 1150

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
