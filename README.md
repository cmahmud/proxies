# SyndProxy private pool

## Current pool

- Alive now: 817
- Gold now: 349
- HTTP: 251 alive / 79 gold
- HTTPS: 150 alive / 21 gold
- SOCKS4: 195 alive / 119 gold
- SOCKS5: 221 alive / 130 gold

## Historical pool

- Discovered: 167924
- Ever alive: 32593
- Ever gold: 1190

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
