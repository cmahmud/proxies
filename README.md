# SyndProxy private pool

## Current pool

- Alive now: 1020
- Gold now: 512
- HTTP: 333 alive / 148 gold
- HTTPS: 259 alive / 90 gold
- SOCKS4: 223 alive / 149 gold
- SOCKS5: 205 alive / 125 gold

## Historical pool

- Discovered: 117156
- Ever alive: 17612
- Ever gold: 692

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
