# SyndProxy private pool

## Current pool

- Alive now: 727
- Gold now: 368
- HTTP: 186 alive / 70 gold
- HTTPS: 148 alive / 17 gold
- SOCKS4: 193 alive / 145 gold
- SOCKS5: 200 alive / 136 gold

## Historical pool

- Discovered: 147649
- Ever alive: 25880
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
