# SyndProxy private pool

## Current pool

- Alive now: 800
- Gold now: 421
- HTTP: 205 alive / 96 gold
- HTTPS: 134 alive / 29 gold
- SOCKS4: 213 alive / 132 gold
- SOCKS5: 248 alive / 164 gold

## Historical pool

- Discovered: 163856
- Ever alive: 31957
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
