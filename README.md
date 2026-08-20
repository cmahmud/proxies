# SyndProxy private pool

## Current pool

- Alive now: 675
- Gold now: 389
- HTTP: 158 alive / 68 gold
- HTTPS: 89 alive / 16 gold
- SOCKS4: 204 alive / 143 gold
- SOCKS5: 224 alive / 162 gold

## Historical pool

- Discovered: 147177
- Ever alive: 25792
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
