# SyndProxy private pool

## Current pool

- Alive now: 889
- Gold now: 402
- HTTP: 259 alive / 89 gold
- HTTPS: 186 alive / 18 gold
- SOCKS4: 214 alive / 152 gold
- SOCKS5: 230 alive / 143 gold

## Historical pool

- Discovered: 155696
- Ever alive: 29276
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
