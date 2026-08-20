# SyndProxy private pool

## Current pool

- Alive now: 694
- Gold now: 385
- HTTP: 170 alive / 67 gold
- HTTPS: 92 alive / 15 gold
- SOCKS4: 200 alive / 142 gold
- SOCKS5: 232 alive / 161 gold

## Historical pool

- Discovered: 147177
- Ever alive: 25792
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
