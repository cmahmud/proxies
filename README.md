# SyndProxy private pool

## Current pool

- Alive now: 824
- Gold now: 395
- HTTP: 207 alive / 73 gold
- HTTPS: 171 alive / 18 gold
- SOCKS4: 222 alive / 150 gold
- SOCKS5: 224 alive / 154 gold

## Historical pool

- Discovered: 151061
- Ever alive: 27370
- Ever gold: 1095

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
