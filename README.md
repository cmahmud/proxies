# SyndProxy private pool

## Current pool

- Alive now: 748
- Gold now: 367
- HTTP: 179 alive / 73 gold
- HTTPS: 145 alive / 16 gold
- SOCKS4: 194 alive / 118 gold
- SOCKS5: 230 alive / 160 gold

## Historical pool

- Discovered: 148333
- Ever alive: 26123
- Ever gold: 1079

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
