# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 380
- HTTP: 97 alive / 59 gold
- HTTPS: 37 alive / 9 gold
- SOCKS4: 172 alive / 157 gold
- SOCKS5: 196 alive / 155 gold

## Historical pool

- Discovered: 174803
- Ever alive: 33093
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
