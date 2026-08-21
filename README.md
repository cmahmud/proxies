# SyndProxy private pool

## Current pool

- Alive now: 794
- Gold now: 404
- HTTP: 205 alive / 85 gold
- HTTPS: 137 alive / 21 gold
- SOCKS4: 220 alive / 152 gold
- SOCKS5: 232 alive / 146 gold

## Historical pool

- Discovered: 155683
- Ever alive: 29208
- Ever gold: 1124

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
