# SyndProxy private pool

## Current pool

- Alive now: 939
- Gold now: 394
- HTTP: 289 alive / 83 gold
- HTTPS: 212 alive / 24 gold
- SOCKS4: 224 alive / 144 gold
- SOCKS5: 214 alive / 143 gold

## Historical pool

- Discovered: 151072
- Ever alive: 27475
- Ever gold: 1097

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
