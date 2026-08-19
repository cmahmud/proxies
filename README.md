# SyndProxy private pool

## Current pool

- Alive now: 812
- Gold now: 355
- HTTP: 258 alive / 82 gold
- HTTPS: 151 alive / 17 gold
- SOCKS4: 211 alive / 141 gold
- SOCKS5: 192 alive / 115 gold

## Historical pool

- Discovered: 119831
- Ever alive: 18320
- Ever gold: 718

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
