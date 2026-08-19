# SyndProxy private pool

## Current pool

- Alive now: 1075
- Gold now: 533
- HTTP: 386 alive / 158 gold
- HTTPS: 257 alive / 90 gold
- SOCKS4: 211 alive / 136 gold
- SOCKS5: 221 alive / 149 gold

## Historical pool

- Discovered: 122388
- Ever alive: 18684
- Ever gold: 728

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
