# SyndProxy private pool

## Current pool

- Alive now: 1079
- Gold now: 425
- HTTP: 382 alive / 96 gold
- HTTPS: 245 alive / 36 gold
- SOCKS4: 205 alive / 131 gold
- SOCKS5: 247 alive / 162 gold

## Historical pool

- Discovered: 161344
- Ever alive: 31131
- Ever gold: 1155

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
