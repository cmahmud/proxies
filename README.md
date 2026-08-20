# SyndProxy private pool

## Current pool

- Alive now: 848
- Gold now: 402
- HTTP: 227 alive / 79 gold
- HTTPS: 162 alive / 23 gold
- SOCKS4: 222 alive / 146 gold
- SOCKS5: 237 alive / 154 gold

## Historical pool

- Discovered: 151071
- Ever alive: 27456
- Ever gold: 1097

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
