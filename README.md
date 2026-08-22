# SyndProxy private pool

## Current pool

- Alive now: 975
- Gold now: 421
- HTTP: 256 alive / 86 gold
- HTTPS: 205 alive / 25 gold
- SOCKS4: 231 alive / 140 gold
- SOCKS5: 283 alive / 170 gold

## Historical pool

- Discovered: 164944
- Ever alive: 32207
- Ever gold: 1173

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
