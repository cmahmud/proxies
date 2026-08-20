# SyndProxy private pool

## Current pool

- Alive now: 1191
- Gold now: 600
- HTTP: 420 alive / 189 gold
- HTTPS: 297 alive / 101 gold
- SOCKS4: 225 alive / 146 gold
- SOCKS5: 249 alive / 164 gold

## Historical pool

- Discovered: 138957
- Ever alive: 23464
- Ever gold: 921

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
