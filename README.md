# SyndProxy private pool

## Current pool

- Alive now: 950
- Gold now: 380
- HTTP: 320 alive / 79 gold
- HTTPS: 197 alive / 25 gold
- SOCKS4: 194 alive / 123 gold
- SOCKS5: 239 alive / 153 gold

## Historical pool

- Discovered: 164975
- Ever alive: 32263
- Ever gold: 1177

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
