# SyndProxy private pool

## Current pool

- Alive now: 658
- Gold now: 211
- HTTP: 155 alive / 25 gold
- HTTPS: 116 alive / 7 gold
- SOCKS4: 172 alive / 98 gold
- SOCKS5: 215 alive / 81 gold

## Historical pool

- Discovered: 91718
- Ever alive: 8682
- Ever gold: 354

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
