# SyndProxy private pool

## Current pool

- Alive now: 737
- Gold now: 368
- HTTP: 194 alive / 68 gold
- HTTPS: 134 alive / 16 gold
- SOCKS4: 188 alive / 143 gold
- SOCKS5: 221 alive / 141 gold

## Historical pool

- Discovered: 147648
- Ever alive: 25876
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
