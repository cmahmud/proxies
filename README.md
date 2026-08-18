# SyndProxy private pool

## Current pool

- Alive now: 691
- Gold now: 210
- HTTP: 161 alive / 24 gold
- HTTPS: 129 alive / 7 gold
- SOCKS4: 176 alive / 99 gold
- SOCKS5: 225 alive / 80 gold

## Historical pool

- Discovered: 91718
- Ever alive: 8682
- Ever gold: 354

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
