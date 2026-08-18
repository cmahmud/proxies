# SyndProxy private pool

## Current pool

- Alive now: 861
- Gold now: 285
- HTTP: 296 alive / 39 gold
- HTTPS: 154 alive / 9 gold
- SOCKS4: 228 alive / 141 gold
- SOCKS5: 183 alive / 96 gold

## Historical pool

- Discovered: 102887
- Ever alive: 13824
- Ever gold: 430

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
