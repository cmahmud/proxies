# SyndProxy private pool

## Current pool

- Alive now: 738
- Gold now: 376
- HTTP: 202 alive / 76 gold
- HTTPS: 121 alive / 18 gold
- SOCKS4: 191 alive / 135 gold
- SOCKS5: 224 alive / 147 gold

## Historical pool

- Discovered: 146130
- Ever alive: 25610
- Ever gold: 1069

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
