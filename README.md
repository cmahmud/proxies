# SyndProxy private pool

## Current pool

- Alive now: 854
- Gold now: 403
- HTTP: 228 alive / 79 gold
- HTTPS: 172 alive / 23 gold
- SOCKS4: 219 alive / 147 gold
- SOCKS5: 235 alive / 154 gold

## Historical pool

- Discovered: 151071
- Ever alive: 27456
- Ever gold: 1097

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
