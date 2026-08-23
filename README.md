# SyndProxy validated proxy pool

## Current pool

- Alive now: 585
- Gold now: 201
- HTTP: 209 alive / 37 gold
- HTTPS: 39 alive / 7 gold
- SOCKS4: 182 alive / 69 gold
- SOCKS5: 155 alive / 88 gold

## Historical pool

- Discovered: 170566
- Ever alive: 32769
- Ever gold: 1209

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
