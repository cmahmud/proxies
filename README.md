# SyndProxy validated proxy pool

## Current pool

- Alive now: 478
- Gold now: 385
- HTTP: 94 alive / 69 gold
- HTTPS: 43 alive / 15 gold
- SOCKS4: 169 alive / 150 gold
- SOCKS5: 172 alive / 151 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48178
- Ever gold: 1521

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
