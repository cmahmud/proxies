# SyndProxy private pool

## Current pool

- Alive now: 842
- Gold now: 364
- HTTP: 239 alive / 87 gold
- HTTPS: 182 alive / 15 gold
- SOCKS4: 210 alive / 140 gold
- SOCKS5: 211 alive / 122 gold

## Historical pool

- Discovered: 119831
- Ever alive: 18285
- Ever gold: 718

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
