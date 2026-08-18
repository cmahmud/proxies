# SyndProxy private pool

## Current pool

- Alive now: 989
- Gold now: 323
- HTTP: 319 alive / 37 gold
- HTTPS: 202 alive / 9 gold
- SOCKS4: 240 alive / 145 gold
- SOCKS5: 228 alive / 132 gold

## Historical pool

- Discovered: 106888
- Ever alive: 14121
- Ever gold: 435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
