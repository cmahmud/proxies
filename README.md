# SyndProxy private pool

## Current pool

- Alive now: 972
- Gold now: 375
- HTTP: 320 alive / 79 gold
- HTTPS: 212 alive / 22 gold
- SOCKS4: 209 alive / 137 gold
- SOCKS5: 231 alive / 137 gold

## Historical pool

- Discovered: 144770
- Ever alive: 25299
- Ever gold: 1057

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
