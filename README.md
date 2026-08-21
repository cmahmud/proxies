# SyndProxy private pool

## Current pool

- Alive now: 1046
- Gold now: 414
- HTTP: 360 alive / 109 gold
- HTTPS: 247 alive / 27 gold
- SOCKS4: 237 alive / 152 gold
- SOCKS5: 202 alive / 126 gold

## Historical pool

- Discovered: 160027
- Ever alive: 30584
- Ever gold: 1146

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
