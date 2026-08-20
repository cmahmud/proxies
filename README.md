# SyndProxy private pool

## Current pool

- Alive now: 664
- Gold now: 382
- HTTP: 172 alive / 75 gold
- HTTPS: 104 alive / 22 gold
- SOCKS4: 200 alive / 144 gold
- SOCKS5: 188 alive / 141 gold

## Historical pool

- Discovered: 146130
- Ever alive: 25645
- Ever gold: 1071

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
