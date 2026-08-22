# SyndProxy private pool

## Current pool

- Alive now: 951
- Gold now: 397
- HTTP: 272 alive / 78 gold
- HTTPS: 219 alive / 27 gold
- SOCKS4: 209 alive / 127 gold
- SOCKS5: 251 alive / 165 gold

## Historical pool

- Discovered: 164962
- Ever alive: 32242
- Ever gold: 1177

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
