# SyndProxy private pool

## Current pool

- Alive now: 928
- Gold now: 373
- HTTP: 290 alive / 70 gold
- HTTPS: 205 alive / 21 gold
- SOCKS4: 211 alive / 141 gold
- SOCKS5: 222 alive / 141 gold

## Historical pool

- Discovered: 149502
- Ever alive: 26736
- Ever gold: 1087

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
