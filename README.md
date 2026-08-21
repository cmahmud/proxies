# SyndProxy private pool

## Current pool

- Alive now: 803
- Gold now: 401
- HTTP: 209 alive / 85 gold
- HTTPS: 132 alive / 24 gold
- SOCKS4: 221 alive / 136 gold
- SOCKS5: 241 alive / 156 gold

## Historical pool

- Discovered: 154727
- Ever alive: 29159
- Ever gold: 1124

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
