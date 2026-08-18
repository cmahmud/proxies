# SyndProxy private pool

## Current pool

- Alive now: 934
- Gold now: 318
- HTTP: 318 alive / 41 gold
- HTTPS: 154 alive / 10 gold
- SOCKS4: 241 alive / 140 gold
- SOCKS5: 221 alive / 127 gold

## Historical pool

- Discovered: 107013
- Ever alive: 14338
- Ever gold: 440

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
