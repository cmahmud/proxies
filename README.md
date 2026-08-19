# SyndProxy private pool

## Current pool

- Alive now: 1036
- Gold now: 526
- HTTP: 359 alive / 154 gold
- HTTPS: 242 alive / 89 gold
- SOCKS4: 223 alive / 149 gold
- SOCKS5: 212 alive / 134 gold

## Historical pool

- Discovered: 117176
- Ever alive: 17715
- Ever gold: 692

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
