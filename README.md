# SyndProxy private pool

## Current pool

- Alive now: 612
- Gold now: 213
- HTTP: 161 alive / 27 gold
- HTTPS: 87 alive / 7 gold
- SOCKS4: 161 alive / 97 gold
- SOCKS5: 203 alive / 82 gold

## Historical pool

- Discovered: 91718
- Ever alive: 8682
- Ever gold: 354

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
