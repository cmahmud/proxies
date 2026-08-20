# SyndProxy private pool

## Current pool

- Alive now: 708
- Gold now: 384
- HTTP: 190 alive / 72 gold
- HTTPS: 115 alive / 17 gold
- SOCKS4: 210 alive / 153 gold
- SOCKS5: 193 alive / 142 gold

## Historical pool

- Discovered: 146130
- Ever alive: 25622
- Ever gold: 1071

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
