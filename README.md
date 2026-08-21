# SyndProxy private pool

## Current pool

- Alive now: 799
- Gold now: 353
- HTTP: 256 alive / 94 gold
- HTTPS: 158 alive / 21 gold
- SOCKS4: 187 alive / 134 gold
- SOCKS5: 198 alive / 104 gold

## Historical pool

- Discovered: 154658
- Ever alive: 28952
- Ever gold: 1117

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
