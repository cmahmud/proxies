# SyndProxy private pool

## Current pool

- Alive now: 828
- Gold now: 414
- HTTP: 224 alive / 85 gold
- HTTPS: 135 alive / 22 gold
- SOCKS4: 224 alive / 153 gold
- SOCKS5: 245 alive / 154 gold

## Historical pool

- Discovered: 155685
- Ever alive: 29214
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
