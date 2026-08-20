# SyndProxy private pool

## Current pool

- Alive now: 817
- Gold now: 398
- HTTP: 214 alive / 73 gold
- HTTPS: 162 alive / 20 gold
- SOCKS4: 221 alive / 150 gold
- SOCKS5: 220 alive / 155 gold

## Historical pool

- Discovered: 151061
- Ever alive: 27370
- Ever gold: 1095

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
