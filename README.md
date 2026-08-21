# SyndProxy private pool

## Current pool

- Alive now: 727
- Gold now: 393
- HTTP: 178 alive / 85 gold
- HTTPS: 124 alive / 20 gold
- SOCKS4: 212 alive / 136 gold
- SOCKS5: 213 alive / 152 gold

## Historical pool

- Discovered: 154732
- Ever alive: 29182
- Ever gold: 1124

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
