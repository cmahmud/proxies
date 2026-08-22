# SyndProxy private pool

## Current pool

- Alive now: 783
- Gold now: 400
- HTTP: 207 alive / 80 gold
- HTTPS: 146 alive / 27 gold
- SOCKS4: 189 alive / 137 gold
- SOCKS5: 241 alive / 156 gold

## Historical pool

- Discovered: 163376
- Ever alive: 31904
- Ever gold: 1169

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
