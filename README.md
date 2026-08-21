# SyndProxy private pool

## Current pool

- Alive now: 969
- Gold now: 412
- HTTP: 311 alive / 103 gold
- HTTPS: 202 alive / 28 gold
- SOCKS4: 226 alive / 155 gold
- SOCKS5: 230 alive / 126 gold

## Historical pool

- Discovered: 160353
- Ever alive: 30817
- Ever gold: 1149

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
