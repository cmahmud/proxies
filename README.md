# SyndProxy private pool

## Current pool

- Alive now: 1012
- Gold now: 371
- HTTP: 354 alive / 97 gold
- HTTPS: 258 alive / 25 gold
- SOCKS4: 182 alive / 116 gold
- SOCKS5: 218 alive / 133 gold

## Historical pool

- Discovered: 153747
- Ever alive: 28820
- Ever gold: 1114

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
