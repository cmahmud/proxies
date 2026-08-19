# SyndProxy private pool

## Current pool

- Alive now: 870
- Gold now: 354
- HTTP: 283 alive / 81 gold
- HTTPS: 175 alive / 17 gold
- SOCKS4: 213 alive / 142 gold
- SOCKS5: 199 alive / 114 gold

## Historical pool

- Discovered: 119831
- Ever alive: 18342
- Ever gold: 718

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
