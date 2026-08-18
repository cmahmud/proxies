# SyndProxy private pool

## Current pool

- Alive now: 975
- Gold now: 255
- HTTP: 394 alive / 29 gold
- HTTPS: 151 alive / 2 gold
- SOCKS4: 201 alive / 119 gold
- SOCKS5: 229 alive / 105 gold

## Historical pool

- Discovered: 99105
- Ever alive: 11747
- Ever gold: 389

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
