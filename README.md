# SyndProxy private pool

## Current pool

- Alive now: 1226
- Gold now: 392
- HTTP: 427 alive / 89 gold
- HTTPS: 331 alive / 14 gold
- SOCKS4: 221 alive / 128 gold
- SOCKS5: 247 alive / 161 gold

## Historical pool

- Discovered: 131851
- Ever alive: 21263
- Ever gold: 880

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
