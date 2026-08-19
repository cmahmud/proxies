# SyndProxy private pool

## Current pool

- Alive now: 1202
- Gold now: 460
- HTTP: 413 alive / 126 gold
- HTTPS: 301 alive / 74 gold
- SOCKS4: 230 alive / 117 gold
- SOCKS5: 258 alive / 143 gold

## Historical pool

- Discovered: 117109
- Ever alive: 17263
- Ever gold: 629

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
