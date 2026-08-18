# SyndProxy private pool

## Current pool

- Alive now: 750
- Gold now: 234
- HTTP: 302 alive / 29 gold
- HTTPS: 71 alive / 7 gold
- SOCKS4: 181 alive / 110 gold
- SOCKS5: 196 alive / 88 gold

## Historical pool

- Discovered: 91718
- Ever alive: 8835
- Ever gold: 354

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
