# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 400
- HTTP: 115 alive / 74 gold
- HTTPS: 48 alive / 15 gold
- SOCKS4: 165 alive / 156 gold
- SOCKS5: 191 alive / 155 gold

## Historical pool

- Discovered: 176974
- Ever alive: 33275
- Ever gold: 1233

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
