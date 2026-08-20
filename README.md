# SyndProxy private pool

## Current pool

- Alive now: 744
- Gold now: 389
- HTTP: 168 alive / 69 gold
- HTTPS: 137 alive / 19 gold
- SOCKS4: 223 alive / 146 gold
- SOCKS5: 216 alive / 155 gold

## Historical pool

- Discovered: 148329
- Ever alive: 26019
- Ever gold: 1077

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
