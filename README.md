# SyndProxy private pool

## Current pool

- Alive now: 1125
- Gold now: 400
- HTTP: 362 alive / 77 gold
- HTTPS: 226 alive / 14 gold
- SOCKS4: 271 alive / 154 gold
- SOCKS5: 266 alive / 155 gold

## Historical pool

- Discovered: 131718
- Ever alive: 20683
- Ever gold: 873

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
