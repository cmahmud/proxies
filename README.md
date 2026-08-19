# SyndProxy private pool

## Current pool

- Alive now: 1181
- Gold now: 409
- HTTP: 368 alive / 97 gold
- HTTPS: 258 alive / 15 gold
- SOCKS4: 247 alive / 150 gold
- SOCKS5: 308 alive / 147 gold

## Historical pool

- Discovered: 131828
- Ever alive: 21101
- Ever gold: 879

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
