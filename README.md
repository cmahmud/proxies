# SyndProxy private pool

## Current pool

- Alive now: 765
- Gold now: 343
- HTTP: 231 alive / 83 gold
- HTTPS: 151 alive / 24 gold
- SOCKS4: 174 alive / 112 gold
- SOCKS5: 209 alive / 124 gold

## Historical pool

- Discovered: 167410
- Ever alive: 32579
- Ever gold: 1190

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
