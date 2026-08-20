# SyndProxy private pool

## Current pool

- Alive now: 697
- Gold now: 384
- HTTP: 178 alive / 72 gold
- HTTPS: 129 alive / 16 gold
- SOCKS4: 182 alive / 137 gold
- SOCKS5: 208 alive / 159 gold

## Historical pool

- Discovered: 146601
- Ever alive: 25673
- Ever gold: 1071

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
