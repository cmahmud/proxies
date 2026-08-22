# SyndProxy private pool

## Current pool

- Alive now: 850
- Gold now: 404
- HTTP: 258 alive / 91 gold
- HTTPS: 154 alive / 27 gold
- SOCKS4: 206 alive / 135 gold
- SOCKS5: 232 alive / 151 gold

## Historical pool

- Discovered: 164921
- Ever alive: 32158
- Ever gold: 1171

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
