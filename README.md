# SyndProxy validated proxy pool

## Current pool

- Alive now: 526
- Gold now: 403
- HTTP: 112 alive / 68 gold
- HTTPS: 47 alive / 13 gold
- SOCKS4: 175 alive / 158 gold
- SOCKS5: 192 alive / 164 gold

## Historical pool

- Discovered: 177985
- Ever alive: 33330
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
