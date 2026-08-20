# SyndProxy private pool

## Current pool

- Alive now: 799
- Gold now: 370
- HTTP: 201 alive / 77 gold
- HTTPS: 183 alive / 17 gold
- SOCKS4: 189 alive / 119 gold
- SOCKS5: 226 alive / 157 gold

## Historical pool

- Discovered: 148333
- Ever alive: 26134
- Ever gold: 1079

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
