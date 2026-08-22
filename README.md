# SyndProxy private pool

## Current pool

- Alive now: 885
- Gold now: 379
- HTTP: 265 alive / 78 gold
- HTTPS: 197 alive / 23 gold
- SOCKS4: 192 alive / 124 gold
- SOCKS5: 231 alive / 154 gold

## Historical pool

- Discovered: 164972
- Ever alive: 32256
- Ever gold: 1177

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
