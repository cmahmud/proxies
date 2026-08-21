# SyndProxy private pool

## Current pool

- Alive now: 964
- Gold now: 406
- HTTP: 281 alive / 96 gold
- HTTPS: 208 alive / 32 gold
- SOCKS4: 233 alive / 147 gold
- SOCKS5: 242 alive / 131 gold

## Historical pool

- Discovered: 160998
- Ever alive: 30979
- Ever gold: 1153

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
