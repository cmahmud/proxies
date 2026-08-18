# SyndProxy private pool

## Current pool

- Alive now: 654
- Gold now: 212
- HTTP: 153 alive / 26 gold
- HTTPS: 115 alive / 7 gold
- SOCKS4: 174 alive / 99 gold
- SOCKS5: 212 alive / 80 gold

## Historical pool

- Discovered: 91718
- Ever alive: 8682
- Ever gold: 354

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
