# SyndProxy private pool

## Current pool

- Alive now: 1731
- Gold now: 644
- HTTP: 678 alive / 211 gold
- HTTPS: 502 alive / 121 gold
- SOCKS4: 217 alive / 151 gold
- SOCKS5: 334 alive / 161 gold

## Historical pool

- Discovered: 141249
- Ever alive: 24191
- Ever gold: 971

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
