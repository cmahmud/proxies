# SyndProxy private pool

## Current pool

- Alive now: 1684
- Gold now: 644
- HTTP: 642 alive / 213 gold
- HTTPS: 487 alive / 121 gold
- SOCKS4: 221 alive / 151 gold
- SOCKS5: 334 alive / 159 gold

## Historical pool

- Discovered: 141249
- Ever alive: 24193
- Ever gold: 971

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
