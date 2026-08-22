# SyndProxy private pool

## Current pool

- Alive now: 997
- Gold now: 390
- HTTP: 295 alive / 85 gold
- HTTPS: 241 alive / 23 gold
- SOCKS4: 205 alive / 125 gold
- SOCKS5: 256 alive / 157 gold

## Historical pool

- Discovered: 164912
- Ever alive: 32135
- Ever gold: 1171

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
