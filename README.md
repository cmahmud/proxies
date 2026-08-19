# SyndProxy private pool

## Current pool

- Alive now: 1207
- Gold now: 389
- HTTP: 414 alive / 93 gold
- HTTPS: 266 alive / 19 gold
- SOCKS4: 237 alive / 137 gold
- SOCKS5: 290 alive / 140 gold

## Historical pool

- Discovered: 133945
- Ever alive: 21615
- Ever gold: 886

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
