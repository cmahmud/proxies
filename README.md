# SyndProxy private pool

## Current pool

- Alive now: 1820
- Gold now: 657
- HTTP: 712 alive / 212 gold
- HTTPS: 520 alive / 114 gold
- SOCKS4: 245 alive / 159 gold
- SOCKS5: 343 alive / 172 gold

## Historical pool

- Discovered: 141249
- Ever alive: 24183
- Ever gold: 969

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
