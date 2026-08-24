# SyndProxy validated proxy pool

## Current pool

- Alive now: 523
- Gold now: 402
- HTTP: 111 alive / 68 gold
- HTTPS: 45 alive / 13 gold
- SOCKS4: 174 alive / 157 gold
- SOCKS5: 193 alive / 164 gold

## Historical pool

- Discovered: 177985
- Ever alive: 33330
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
