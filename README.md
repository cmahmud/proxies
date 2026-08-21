# SyndProxy private pool

## Current pool

- Alive now: 855
- Gold now: 385
- HTTP: 279 alive / 75 gold
- HTTPS: 136 alive / 21 gold
- SOCKS4: 199 alive / 128 gold
- SOCKS5: 241 alive / 161 gold

## Historical pool

- Discovered: 157412
- Ever alive: 29697
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
