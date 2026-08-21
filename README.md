# SyndProxy private pool

## Current pool

- Alive now: 996
- Gold now: 455
- HTTP: 345 alive / 109 gold
- HTTPS: 186 alive / 30 gold
- SOCKS4: 211 alive / 154 gold
- SOCKS5: 254 alive / 162 gold

## Historical pool

- Discovered: 153726
- Ever alive: 28589
- Ever gold: 1110

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
