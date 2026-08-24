# SyndProxy validated proxy pool

## Current pool

- Alive now: 490
- Gold now: 382
- HTTP: 97 alive / 54 gold
- HTTPS: 41 alive / 12 gold
- SOCKS4: 169 alive / 154 gold
- SOCKS5: 183 alive / 162 gold

## Historical pool

- Discovered: 179377
- Ever alive: 33469
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
