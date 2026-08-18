# SyndProxy private pool

## Current pool

- Alive now: 574
- Gold now: 221
- HTTP: 152 alive / 32 gold
- HTTPS: 76 alive / 8 gold
- SOCKS4: 149 alive / 99 gold
- SOCKS5: 197 alive / 82 gold

## Historical pool

- Discovered: 91718
- Ever alive: 8682
- Ever gold: 354

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
