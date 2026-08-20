# SyndProxy private pool

## Current pool

- Alive now: 830
- Gold now: 404
- HTTP: 239 alive / 83 gold
- HTTPS: 182 alive / 23 gold
- SOCKS4: 205 alive / 148 gold
- SOCKS5: 204 alive / 150 gold

## Historical pool

- Discovered: 151050
- Ever alive: 27167
- Ever gold: 1092

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
