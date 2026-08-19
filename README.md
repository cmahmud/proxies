# SyndProxy private pool

## Current pool

- Alive now: 948
- Gold now: 344
- HTTP: 325 alive / 67 gold
- HTTPS: 191 alive / 16 gold
- SOCKS4: 192 alive / 111 gold
- SOCKS5: 240 alive / 150 gold

## Historical pool

- Discovered: 111011
- Ever alive: 16110
- Ever gold: 508

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
