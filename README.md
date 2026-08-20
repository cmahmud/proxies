# SyndProxy private pool

## Current pool

- Alive now: 709
- Gold now: 383
- HTTP: 193 alive / 72 gold
- HTTPS: 103 alive / 16 gold
- SOCKS4: 214 alive / 153 gold
- SOCKS5: 199 alive / 142 gold

## Historical pool

- Discovered: 146130
- Ever alive: 25622
- Ever gold: 1071

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
