# SyndProxy private pool

## Current pool

- Alive now: 882
- Gold now: 368
- HTTP: 285 alive / 96 gold
- HTTPS: 173 alive / 28 gold
- SOCKS4: 215 alive / 137 gold
- SOCKS5: 209 alive / 107 gold

## Historical pool

- Discovered: 154713
- Ever alive: 28971
- Ever gold: 1117

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
