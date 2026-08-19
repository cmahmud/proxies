# SyndProxy private pool

## Current pool

- Alive now: 1094
- Gold now: 512
- HTTP: 384 alive / 146 gold
- HTTPS: 274 alive / 92 gold
- SOCKS4: 223 alive / 144 gold
- SOCKS5: 213 alive / 130 gold

## Historical pool

- Discovered: 117170
- Ever alive: 17690
- Ever gold: 692

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
