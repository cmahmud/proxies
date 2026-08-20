# SyndProxy private pool

## Current pool

- Alive now: 1804
- Gold now: 642
- HTTP: 735 alive / 221 gold
- HTTPS: 520 alive / 117 gold
- SOCKS4: 217 alive / 145 gold
- SOCKS5: 332 alive / 159 gold

## Historical pool

- Discovered: 141249
- Ever alive: 24195
- Ever gold: 971

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
