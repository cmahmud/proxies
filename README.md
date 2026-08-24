# SyndProxy validated proxy pool

## Current pool

- Alive now: 494
- Gold now: 392
- HTTP: 91 alive / 55 gold
- HTTPS: 49 alive / 15 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 185 alive / 163 gold

## Historical pool

- Discovered: 179378
- Ever alive: 33489
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
