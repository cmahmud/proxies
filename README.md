# SyndProxy private pool

## Current pool

- Alive now: 826
- Gold now: 353
- HTTP: 260 alive / 81 gold
- HTTPS: 162 alive / 17 gold
- SOCKS4: 211 alive / 141 gold
- SOCKS5: 193 alive / 114 gold

## Historical pool

- Discovered: 119831
- Ever alive: 18332
- Ever gold: 718

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
