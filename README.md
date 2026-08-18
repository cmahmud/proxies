# SyndProxy private pool

## Current pool

- Alive now: 581
- Gold now: 220
- HTTP: 155 alive / 31 gold
- HTTPS: 78 alive / 8 gold
- SOCKS4: 155 alive / 98 gold
- SOCKS5: 193 alive / 83 gold

## Historical pool

- Discovered: 91718
- Ever alive: 8682
- Ever gold: 354

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
