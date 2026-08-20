# SyndProxy private pool

## Current pool

- Alive now: 1552
- Gold now: 445
- HTTP: 580 alive / 123 gold
- HTTPS: 381 alive / 35 gold
- SOCKS4: 254 alive / 132 gold
- SOCKS5: 337 alive / 155 gold

## Historical pool

- Discovered: 136248
- Ever alive: 22683
- Ever gold: 909

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
