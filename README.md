# SyndProxy private pool

## Current pool

- Alive now: 928
- Gold now: 367
- HTTP: 300 alive / 70 gold
- HTTPS: 192 alive / 19 gold
- SOCKS4: 190 alive / 120 gold
- SOCKS5: 246 alive / 158 gold

## Historical pool

- Discovered: 148333
- Ever alive: 26099
- Ever gold: 1079

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
