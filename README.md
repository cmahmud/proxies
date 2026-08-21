# SyndProxy private pool

## Current pool

- Alive now: 1043
- Gold now: 363
- HTTP: 368 alive / 82 gold
- HTTPS: 264 alive / 18 gold
- SOCKS4: 181 alive / 116 gold
- SOCKS5: 230 alive / 147 gold

## Historical pool

- Discovered: 158225
- Ever alive: 29878
- Ever gold: 1138

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
