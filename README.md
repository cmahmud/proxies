# SyndProxy validated proxy pool

## Current pool

- Alive now: 544
- Gold now: 418
- HTTP: 94 alive / 63 gold
- HTTPS: 76 alive / 21 gold
- SOCKS4: 178 alive / 163 gold
- SOCKS5: 196 alive / 171 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36118
- Ever gold: 1267

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
