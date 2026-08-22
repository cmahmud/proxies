# SyndProxy private pool

## Current pool

- Alive now: 861
- Gold now: 409
- HTTP: 252 alive / 89 gold
- HTTPS: 153 alive / 27 gold
- SOCKS4: 206 alive / 128 gold
- SOCKS5: 250 alive / 165 gold

## Historical pool

- Discovered: 164921
- Ever alive: 32158
- Ever gold: 1171

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
