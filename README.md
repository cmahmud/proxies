# SyndProxy private pool

## Current pool

- Alive now: 778
- Gold now: 376
- HTTP: 222 alive / 78 gold
- HTTPS: 128 alive / 20 gold
- SOCKS4: 192 alive / 133 gold
- SOCKS5: 236 alive / 145 gold

## Historical pool

- Discovered: 146130
- Ever alive: 25610
- Ever gold: 1069

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
