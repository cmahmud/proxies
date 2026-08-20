# SyndProxy private pool

## Current pool

- Alive now: 872
- Gold now: 406
- HTTP: 243 alive / 76 gold
- HTTPS: 192 alive / 22 gold
- SOCKS4: 211 alive / 149 gold
- SOCKS5: 226 alive / 159 gold

## Historical pool

- Discovered: 151050
- Ever alive: 27155
- Ever gold: 1092

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
