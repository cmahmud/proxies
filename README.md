# SyndProxy validated proxy pool

## Current pool

- Alive now: 510
- Gold now: 404
- HTTP: 109 alive / 69 gold
- HTTPS: 49 alive / 15 gold
- SOCKS4: 171 alive / 158 gold
- SOCKS5: 181 alive / 162 gold

## Historical pool

- Discovered: 177314
- Ever alive: 33277
- Ever gold: 1233

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
