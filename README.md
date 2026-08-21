# SyndProxy private pool

## Current pool

- Alive now: 787
- Gold now: 402
- HTTP: 206 alive / 89 gold
- HTTPS: 126 alive / 24 gold
- SOCKS4: 214 alive / 136 gold
- SOCKS5: 241 alive / 153 gold

## Historical pool

- Discovered: 154727
- Ever alive: 29169
- Ever gold: 1124

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
