# SyndProxy private pool

## Current pool

- Alive now: 888
- Gold now: 398
- HTTP: 237 alive / 73 gold
- HTTPS: 185 alive / 24 gold
- SOCKS4: 228 alive / 147 gold
- SOCKS5: 238 alive / 154 gold

## Historical pool

- Discovered: 151071
- Ever alive: 27460
- Ever gold: 1097

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
