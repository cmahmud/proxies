# SyndProxy private pool

## Current pool

- Alive now: 1068
- Gold now: 403
- HTTP: 383 alive / 106 gold
- HTTPS: 225 alive / 25 gold
- SOCKS4: 226 alive / 132 gold
- SOCKS5: 234 alive / 140 gold

## Historical pool

- Discovered: 160027
- Ever alive: 30612
- Ever gold: 1146

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
