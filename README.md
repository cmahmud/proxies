# SyndProxy private pool

## Current pool

- Alive now: 869
- Gold now: 398
- HTTP: 218 alive / 73 gold
- HTTPS: 194 alive / 25 gold
- SOCKS4: 226 alive / 147 gold
- SOCKS5: 231 alive / 153 gold

## Historical pool

- Discovered: 151072
- Ever alive: 27462
- Ever gold: 1097

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
