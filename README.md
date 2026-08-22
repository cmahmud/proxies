# SyndProxy private pool

## Current pool

- Alive now: 1310
- Gold now: 411
- HTTP: 536 alive / 96 gold
- HTTPS: 321 alive / 32 gold
- SOCKS4: 222 alive / 140 gold
- SOCKS5: 231 alive / 143 gold

## Historical pool

- Discovered: 163250
- Ever alive: 31727
- Ever gold: 1165

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
