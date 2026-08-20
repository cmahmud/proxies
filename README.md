# SyndProxy private pool

## Current pool

- Alive now: 839
- Gold now: 404
- HTTP: 232 alive / 74 gold
- HTTPS: 151 alive / 20 gold
- SOCKS4: 225 alive / 152 gold
- SOCKS5: 231 alive / 158 gold

## Historical pool

- Discovered: 148329
- Ever alive: 26028
- Ever gold: 1077

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
