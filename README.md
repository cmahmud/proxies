# SyndProxy private pool

## Current pool

- Alive now: 873
- Gold now: 405
- HTTP: 217 alive / 82 gold
- HTTPS: 162 alive / 24 gold
- SOCKS4: 223 alive / 145 gold
- SOCKS5: 271 alive / 154 gold

## Historical pool

- Discovered: 151071
- Ever alive: 27443
- Ever gold: 1097

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
