# SyndProxy private pool

## Current pool

- Alive now: 856
- Gold now: 406
- HTTP: 235 alive / 82 gold
- HTTPS: 157 alive / 24 gold
- SOCKS4: 223 alive / 146 gold
- SOCKS5: 241 alive / 154 gold

## Historical pool

- Discovered: 151071
- Ever alive: 27449
- Ever gold: 1097

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
