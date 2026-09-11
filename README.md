# SyndProxy validated proxy pool

## Current pool

- Alive now: 723
- Gold now: 346
- HTTP: 174 alive / 81 gold
- HTTPS: 112 alive / 39 gold
- SOCKS4: 102 alive / 53 gold
- SOCKS5: 335 alive / 173 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48552
- Ever gold: 1543

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
