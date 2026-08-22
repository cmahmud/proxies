# SyndProxy private pool

## Current pool

- Alive now: 1082
- Gold now: 423
- HTTP: 390 alive / 96 gold
- HTTPS: 250 alive / 35 gold
- SOCKS4: 198 alive / 131 gold
- SOCKS5: 244 alive / 161 gold

## Historical pool

- Discovered: 161344
- Ever alive: 31130
- Ever gold: 1155

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
