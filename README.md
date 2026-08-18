# SyndProxy private pool

## Current pool

- Alive now: 600
- Gold now: 216
- HTTP: 153 alive / 29 gold
- HTTPS: 89 alive / 7 gold
- SOCKS4: 158 alive / 97 gold
- SOCKS5: 200 alive / 83 gold

## Historical pool

- Discovered: 91718
- Ever alive: 8682
- Ever gold: 354

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
