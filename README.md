# SyndProxy validated proxy pool

## Current pool

- Alive now: 486
- Gold now: 382
- HTTP: 94 alive / 53 gold
- HTTPS: 37 alive / 12 gold
- SOCKS4: 173 alive / 154 gold
- SOCKS5: 182 alive / 163 gold

## Historical pool

- Discovered: 179377
- Ever alive: 33469
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
