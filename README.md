# SyndProxy validated proxy pool

## Current pool

- Alive now: 500
- Gold now: 380
- HTTP: 97 alive / 58 gold
- HTTPS: 35 alive / 10 gold
- SOCKS4: 172 alive / 158 gold
- SOCKS5: 196 alive / 154 gold

## Historical pool

- Discovered: 174811
- Ever alive: 33093
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
