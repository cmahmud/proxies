# SyndProxy private pool

## Current pool

- Alive now: 718
- Gold now: 387
- HTTP: 150 alive / 69 gold
- HTTPS: 136 alive / 16 gold
- SOCKS4: 223 alive / 147 gold
- SOCKS5: 209 alive / 155 gold

## Historical pool

- Discovered: 148329
- Ever alive: 26011
- Ever gold: 1077

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
